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
    s = '''sudo nmcli con add type vlan con-name {name} dev eno2 id {vlan} connection.interface-name {name} ipv4.addresses 172.16.{number}.1/24 ipv4.method manual ipv6.method disabled
    '''.format(number=x+200, name=interfaces[x], vlan=x+300)
    print(s)

"""
Example output

sudo nmcli con add type vlan con-name kitchen_a dev eno2 id 300 connection.interface-name kitchen_a ipv4.addresses 172.16.200.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_b dev eno2 id 301 connection.interface-name kitchen_b ipv4.addresses 172.16.201.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_c dev eno2 id 302 connection.interface-name kitchen_c ipv4.addresses 172.16.202.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_d dev eno2 id 303 connection.interface-name kitchen_d ipv4.addresses 172.16.203.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_e dev eno2 id 304 connection.interface-name kitchen_e ipv4.addresses 172.16.204.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_f dev eno2 id 305 connection.interface-name kitchen_f ipv4.addresses 172.16.205.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_g dev eno2 id 306 connection.interface-name kitchen_g ipv4.addresses 172.16.206.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_h dev eno2 id 307 connection.interface-name kitchen_h ipv4.addresses 172.16.207.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_i dev eno2 id 308 connection.interface-name kitchen_i ipv4.addresses 172.16.208.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_j dev eno2 id 309 connection.interface-name kitchen_j ipv4.addresses 172.16.209.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_k dev eno2 id 310 connection.interface-name kitchen_k ipv4.addresses 172.16.210.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_l dev eno2 id 311 connection.interface-name kitchen_l ipv4.addresses 172.16.211.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_m dev eno2 id 312 connection.interface-name kitchen_m ipv4.addresses 172.16.212.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_n dev eno2 id 313 connection.interface-name kitchen_n ipv4.addresses 172.16.213.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_o dev eno2 id 314 connection.interface-name kitchen_o ipv4.addresses 172.16.214.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_p dev eno2 id 315 connection.interface-name kitchen_p ipv4.addresses 172.16.215.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_q dev eno2 id 316 connection.interface-name kitchen_q ipv4.addresses 172.16.216.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_r dev eno2 id 317 connection.interface-name kitchen_r ipv4.addresses 172.16.217.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_s dev eno2 id 318 connection.interface-name kitchen_s ipv4.addresses 172.16.218.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_t dev eno2 id 319 connection.interface-name kitchen_t ipv4.addresses 172.16.219.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_u dev eno2 id 320 connection.interface-name kitchen_u ipv4.addresses 172.16.220.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_v dev eno2 id 321 connection.interface-name kitchen_v ipv4.addresses 172.16.221.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_x dev eno2 id 322 connection.interface-name kitchen_x ipv4.addresses 172.16.222.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name kitchen_y dev eno2 id 323 connection.interface-name kitchen_y ipv4.addresses 172.16.223.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name falladen dev eno2 id 324 connection.interface-name falladen ipv4.addresses 172.16.224.1/24 ipv4.method manual ipv6.method disabled
    
sudo nmcli con add type vlan con-name multiroom dev eno2 id 325 connection.interface-name multiroom ipv4.addresses 172.16.225.1/24 ipv4.method manual ipv6.method disabled
"""