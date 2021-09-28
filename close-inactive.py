# Import everything from our webapp
from common import get_logged_in_ips
import re
import subprocess
import sys
from datetime import datetime
import os

# This is meant to run as a cron job every minute on the captive portal server
# This will check all open ips and close any open ips if arp entry expires in linux. Typical cache is 60 secs.

# How does it work? We expect a format like this for some active interface
# $ ip neigh show dev lan_party to 172.16.190.10
# 172.16.190.10 lladdr ff:ff:ff:ff:ff:ff REACHABLE


for ip in get_logged_in_ips():
    # Prepare regex check
    pattern = re.compile(r'^\?' + re.escape(ip) + ' lladdr ([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2}) REACHABLE')

    # Get current arp status for this interface
    result_raw = subprocess.run(['/usr/sbin/ip', 'neigh', 'show', 'dev', 'lan_party', 'to', ip], stdout=subprocess.PIPE)

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
        save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",system_automatic_close_arp_check_failed,lan_party," + ip + ",\n"

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
        cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'delete element captive open_ips_lan_party { " + ip + " }'")
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
