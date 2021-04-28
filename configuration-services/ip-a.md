# Network configuration

Network configuration should look something like this (generate scripts and help is in the generate subfolder for all but the public interface eno1 that is below this list)


    # ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host 
           valid_lft forever preferred_lft forever
    2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b6 brd ff:ff:ff:ff:ff:ff
        altname enp3s0f0
        inet 82.211.200.202/26 brd 82.211.200.255 scope global noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.8/32 scope global noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.200/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.201/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.203/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.204/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.205/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.206/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.224/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.225/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.207/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.208/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.209/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.210/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.211/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.212/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.213/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.214/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.215/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.216/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.217/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.218/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.219/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.220/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.221/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.222/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
        inet 82.211.200.223/26 brd 82.211.200.255 scope global secondary noprefixroute eno1
           valid_lft forever preferred_lft forever
    3: eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        altname enp3s0f1
    4: eno3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b8 brd ff:ff:ff:ff:ff:ff
        altname enp3s0f2
    5: eno4: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b9 brd ff:ff:ff:ff:ff:ff
        altname enp3s0f3
    26: kitchen_a@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.200.1/24 brd 172.16.200.255 scope global noprefixroute kitchen_a
           valid_lft forever preferred_lft forever
    27: kitchen_b@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.201.1/24 brd 172.16.201.255 scope global noprefixroute kitchen_b
           valid_lft forever preferred_lft forever
    28: kitchen_c@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.202.1/24 brd 172.16.202.255 scope global noprefixroute kitchen_c
           valid_lft forever preferred_lft forever
    29: kitchen_d@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.203.1/24 brd 172.16.203.255 scope global noprefixroute kitchen_d
           valid_lft forever preferred_lft forever
    30: kitchen_e@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.204.1/24 brd 172.16.204.255 scope global noprefixroute kitchen_e
           valid_lft forever preferred_lft forever
    31: kitchen_f@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.205.1/24 brd 172.16.205.255 scope global noprefixroute kitchen_f
           valid_lft forever preferred_lft forever
    32: kitchen_g@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.206.1/24 brd 172.16.206.255 scope global noprefixroute kitchen_g
           valid_lft forever preferred_lft forever
    33: kitchen_h@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.207.1/24 brd 172.16.207.255 scope global noprefixroute kitchen_h
           valid_lft forever preferred_lft forever
    34: kitchen_i@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.208.1/24 brd 172.16.208.255 scope global noprefixroute kitchen_i
           valid_lft forever preferred_lft forever
    35: kitchen_j@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.209.1/24 brd 172.16.209.255 scope global noprefixroute kitchen_j
           valid_lft forever preferred_lft forever
    36: kitchen_k@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.210.1/24 brd 172.16.210.255 scope global noprefixroute kitchen_k
           valid_lft forever preferred_lft forever
    37: kitchen_l@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.211.1/24 brd 172.16.211.255 scope global noprefixroute kitchen_l
           valid_lft forever preferred_lft forever
    38: kitchen_m@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.212.1/24 brd 172.16.212.255 scope global noprefixroute kitchen_m
           valid_lft forever preferred_lft forever
    39: kitchen_n@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.213.1/24 brd 172.16.213.255 scope global noprefixroute kitchen_n
           valid_lft forever preferred_lft forever
    40: kitchen_o@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.214.1/24 brd 172.16.214.255 scope global noprefixroute kitchen_o
           valid_lft forever preferred_lft forever
    41: kitchen_p@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.215.1/24 brd 172.16.215.255 scope global noprefixroute kitchen_p
           valid_lft forever preferred_lft forever
    42: kitchen_q@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.216.1/24 brd 172.16.216.255 scope global noprefixroute kitchen_q
           valid_lft forever preferred_lft forever
    43: kitchen_r@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.217.1/24 brd 172.16.217.255 scope global noprefixroute kitchen_r
           valid_lft forever preferred_lft forever
    44: kitchen_s@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.218.1/24 brd 172.16.218.255 scope global noprefixroute kitchen_s
           valid_lft forever preferred_lft forever
    45: kitchen_t@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.219.1/24 brd 172.16.219.255 scope global noprefixroute kitchen_t
           valid_lft forever preferred_lft forever
    46: kitchen_u@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.220.1/24 brd 172.16.220.255 scope global noprefixroute kitchen_u
           valid_lft forever preferred_lft forever
    47: kitchen_v@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.221.1/24 brd 172.16.221.255 scope global noprefixroute kitchen_v
           valid_lft forever preferred_lft forever
    48: kitchen_x@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.222.1/24 brd 172.16.222.255 scope global noprefixroute kitchen_x
           valid_lft forever preferred_lft forever
    49: kitchen_y@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.223.1/24 brd 172.16.223.255 scope global noprefixroute kitchen_y
           valid_lft forever preferred_lft forever
    50: falladen@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.224.1/24 brd 172.16.224.255 scope global noprefixroute falladen
           valid_lft forever preferred_lft forever
    51: multiroom@eno2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
        link/ether 3c:ec:ef:76:5e:b7 brd ff:ff:ff:ff:ff:ff
        inet 172.16.225.1/24 brd 172.16.225.255 scope global noprefixroute multiroom
           valid_lft forever preferred_lft forever


For the public interface here is the nmcli command to add those easily

    nmcli con mod eno1 ipv4.addresses +ipv4.addresses 82.211.200.200/26, 82.211.200.201/26, 82.211.200.202/26, 82.211.200.203/26, 82.211.200.204/26, 82.211.200.205/26, 82.211.200.206/26, 82.211.200.207/26, 82.211.200.208/26, 82.211.200.209/26, 82.211.200.210/26, 82.211.200.211/26, 82.211.200.212/26, 82.211.200.213/26, 82.211.200.214/26, 82.211.200.215/26, 82.211.200.216/26, 82.211.200.217/26, 82.211.200.218/26, 82.211.200.219/26, 82.211.200.220/26, 82.211.200.221/26, 82.211.200.222/26, 82.211.200.223/26, 82.211.200.224/26, 82.211.200.225/26, 82.211.200.225/26
