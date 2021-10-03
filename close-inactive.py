# Import everything from our webapp
from common import get_open_interfaces, interfaces
import re
import subprocess
import sys
from datetime import datetime
import os

# This is meant to run as a cron job every minute on the captive portal server
# This will check all open interfaces and close any open interface if arp entry expires in linux. Typical cache is 60 secs.

# How does it work? We expect a format like this for some active interface
# $ arp -i kitchen_o -a
# ? (172.16.214.100) at ff:ff:ff:ff:ff:ff [ether] on kitchen_o

# We check that we get an IP from the right interface, with a known mac.


open_interfaces = get_open_interfaces()

for interface_name in open_interfaces:
    # Get interface ID from name (with zero padding)
    interface_id = str(interfaces.index(interface_name)).zfill(2)

    # Prepare regex check
    pattern = re.compile(r'^\? \(172\.16\.2' + interface_id + '\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\) at ([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2}) \[ether\] on ' + interface_name + '$')

    # Get current arp status for this interface
    result_raw = subprocess.run(['/usr/sbin/arp', '-i', interface_name, '-a'], stdout=subprocess.PIPE)

    # Set status to be inactive
    is_active = False

    # Check every line of arp output for match (normally there will only be one line)
    for line in result_raw.stdout.splitlines():
        if bool(pattern.search(line.decode(sys.stdout.encoding))):
            # Match was found, this interface is active, no need to check anything else
            is_active = True
            break

    # Disable interface if it is inactive
    if is_active == False:
        # Make string to save in log file username + vlan id?
        # TODO Add timezone to timestamp. For now it is as system time
        save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",system_automatic_close_arp_check_failed," + interface_name + ",no-ip-arp,\n"

        # Save this string to log file
        log_file_path = '/var/log/pop-captive/'
        current_date = datetime.now().strftime("%Y%m%d")
        log_filename = 'pop-captive-access-' + current_date + '.log'
        log_file = open(log_file_path + log_filename, 'a')
        log_file.write(save_to_log)
        log_file.close()

        # TODO Read log again to be sure it was written correctly

        # Call nft command with sudo to open that network
        # TODO how to handle if this call fails?
        cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'delete element captive open_interfaces { " + interface_name + " }'")
        if os.WEXITSTATUS(cmd) != 0:
            # Log if interface could not be closed

            # Make string to save in log file username + vlan id?
            # TODO Add timezone to timestamp. For now it is as system time
            save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",system_failure_could_not_close_network,lan_party," + ip + ",\n"

            # Save this string to log file
            log_file_path = '/var/log/pop-captive/'
            current_date = datetime.now().strftime("%Y%m%d")
            log_filename = 'pop-captive-access-' + current_date + '.log'
            log_file = open(log_file_path + log_filename, 'a')
            log_file.write(save_to_log)
            log_file.close()
