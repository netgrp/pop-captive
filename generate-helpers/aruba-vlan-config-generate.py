interfaces = [None] * 26

# Note: - used instead of _ in names!
interfaces[0] = "kitchen-a"
interfaces[1] = "kitchen-b"
interfaces[2] = "kitchen-c"
interfaces[3] = "kitchen-d"
interfaces[4] = "kitchen-e"
interfaces[5] = "kitchen-f"
interfaces[6] = "kitchen-g"
interfaces[7] = "kitchen-h"
interfaces[8] = "kitchen-i"
interfaces[9] = "kitchen-j"
interfaces[10] = "kitchen-k"
interfaces[11] = "kitchen-l"
interfaces[12] = "kitchen-m"
interfaces[13] = "kitchen-n"
interfaces[14] = "kitchen-o"
interfaces[15] = "kitchen-p"
interfaces[16] = "kitchen-q"
interfaces[17] = "kitchen-r"
interfaces[18] = "kitchen-s"
interfaces[19] = "kitchen-t"
interfaces[20] = "kitchen-u"
interfaces[21] = "kitchen-v"
interfaces[22] = "kitchen-x"
interfaces[23] = "kitchen-y"
interfaces[24] = "falladen"
interfaces[25] = "multiroom"



for x in range(26):
    s = '''vlan {vlan}
   name "captive-{name}"
   tagged all
   no ip address
   exit'''.format(number=x+200, name=interfaces[x], vlan=x+300)
    print(s)

"""
Example output

vlan 300
   name "captive-kitchen-a"
   tagged all
   no ip address
   exit
vlan 301
   name "captive-kitchen-b"
   tagged all
   no ip address
   exit
vlan 302
   name "captive-kitchen-c"
   tagged all
   no ip address
   exit
vlan 303
   name "captive-kitchen-d"
   tagged all
   no ip address
   exit
vlan 304
   name "captive-kitchen-e"
   tagged all
   no ip address
   exit
vlan 305
   name "captive-kitchen-f"
   tagged all
   no ip address
   exit
vlan 306
   name "captive-kitchen-g"
   tagged all
   no ip address
   exit
vlan 307
   name "captive-kitchen-h"
   tagged all
   no ip address
   exit
vlan 308
   name "captive-kitchen-i"
   tagged all
   no ip address
   exit
vlan 309
   name "captive-kitchen-j"
   tagged all
   no ip address
   exit
vlan 310
   name "captive-kitchen-k"
   tagged all
   no ip address
   exit
vlan 311
   name "captive-kitchen-l"
   tagged all
   no ip address
   exit
vlan 312
   name "captive-kitchen-m"
   tagged all
   no ip address
   exit
vlan 313
   name "captive-kitchen-n"
   tagged all
   no ip address
   exit
vlan 314
   name "captive-kitchen-o"
   tagged all
   no ip address
   exit
vlan 315
   name "captive-kitchen-p"
   tagged all
   no ip address
   exit
vlan 316
   name "captive-kitchen-q"
   tagged all
   no ip address
   exit
vlan 317
   name "captive-kitchen-r"
   tagged all
   no ip address
   exit
vlan 318
   name "captive-kitchen-s"
   tagged all
   no ip address
   exit
vlan 319
   name "captive-kitchen-t"
   tagged all
   no ip address
   exit
vlan 320
   name "captive-kitchen-u"
   tagged all
   no ip address
   exit
vlan 321
   name "captive-kitchen-v"
   tagged all
   no ip address
   exit
vlan 322
   name "captive-kitchen-x"
   tagged all
   no ip address
   exit
vlan 323
   name "captive-kitchen-y"
   tagged all
   no ip address
   exit
vlan 324
   name "captive-falladen"
   tagged all
   no ip address
   exit
vlan 325
   name "captive-multiroom"
   tagged all
   no ip address
   exit

"""
