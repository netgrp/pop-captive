import subprocess
import json



# Get current state, who is logged in? This is defined by what interfaces that are open
# TODO: Cache result for request
def get_logged_in_ips():
    # Get the list of open interfaces from nft
    result_raw = subprocess.run(['/usr/bin/sudo', '/usr/sbin/nft', '-j', 'list', 'set', 'ip', 'captive', 'open_ips_lan_party'], stdout=subprocess.PIPE)

    # Get the output and decode it
    result_json = json.loads(result_raw.stdout)

    # Prepare list for open interfaces
    open_ips = []

    # Extract the interface names for the open interfaces
    if 'elem' in result_json['nftables'][1]['set']:
        for element in result_json['nftables'][1]['set']['elem']:
            open_ips.append(element['elem']['val'])

    return open_ips
