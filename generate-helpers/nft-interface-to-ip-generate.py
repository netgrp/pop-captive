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



for x in range(26):
    s = '''nft 'add element captive interface_to_ip {{ "{name}" : 82.211.200.{number} }}'
    '''.format(number=x+200, name=interfaces[x], vlan=x+300)
    print(s)