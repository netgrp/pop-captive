import subprocess
import json

# Semi-hardcoded configuration variables - START
interfaces = [None] * 26
interfaces[0] = "kitchen_a"
interfaces[1] = "kitchen_b"
interfaces[2] = "kitchen_c"
interfaces[3] = "kitchen_d"
interfaces[4] = "kitchen_e"
interfaces[5] = "kitchen_f"
interfaces[6] = "kitchen_g"
interfaces[7] = "kitchen_h"
interfaces[8] = "kitchen_i"
interfaces[9] = "kitchen_j"
interfaces[10] = "kitchen_k"
interfaces[11] = "kitchen_l"
interfaces[12] = "kitchen_m"
interfaces[13] = "kitchen_n"
interfaces[14] = "kitchen_o"
interfaces[15] = "kitchen_p"
interfaces[16] = "kitchen_q"
interfaces[17] = "kitchen_r"
interfaces[18] = "kitchen_s"
interfaces[19] = "kitchen_t"
interfaces[20] = "kitchen_u"
interfaces[21] = "kitchen_v"
interfaces[22] = "kitchen_x"
interfaces[23] = "kitchen_y"
interfaces[24] = "falladen"
interfaces[25] = "multiroom"

# Get current state, who is logged in? This is defined by what interfaces that are open
# TODO: Cache result for request
def get_open_interfaces():
    # Get the list of open interfaces from nft
    result_raw = subprocess.run(['/usr/bin/sudo', '/usr/sbin/nft', '-j', 'list', 'set', 'inet', 'captive', 'open_interfaces'], stdout=subprocess.PIPE)

    # Get the output and decode it
    result_json = json.loads(result_raw.stdout)

    # Prepare list for open interfaces
    open_interfaces = []

    # Extract the interface names for the open interfaces
    if 'elem' in result_json['nftables'][1]['set']:
        for element in result_json['nftables'][1]['set']['elem']:
            open_interfaces.append(element['elem']['val'])

    return open_interfaces
