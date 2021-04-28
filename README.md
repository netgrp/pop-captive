# pop-captive
Captive Portal P. O. Pedersen Kollegiet for shared network responsibility assignment.

Build to use nftables for as much as possible with a minimal web app on top to handle the required logging and logins.

The captive portal does follow RFC6585. We only redirect port 80 for the captive portal and use code 511 to avoid cache poision/malfunction.

Relevent resources that are used for the captive portal design:
* https://tools.ietf.org/html/rfc6585#section-6
* https://evertpot.com/http/511-network-authentication-required

## Software/Packages required. We use Fedora 34 as a base

* nftables - stateful firewall, NAT, Captive portal DNAT
* isc-dhcp-server - DHCP server
* nginx - webserver proxy front end
* Flask - lightweight web framework

To install this in Fedora. We do not want firewalld

    sudo dnf mark install nftables
    sudo dnf remove firewalld
    sudo dnf install dhcp

## Forward in Linux kernel

Enable ipv4 forward change this file: /etc/sysctl.conf

And add this:

    net.ipv4.ip_forward = 1


Why? For NAT to work we need to be able to forwards packages and make this machine work as a router. If not the server will not forward packages (default behavior in Linux) and there would be no internet connection in the captive portal, only a login page.

Source: https://docs.fedoraproject.org/en-US/Fedora/18/html/Security_Guide/sect-Security_Guide-Firewalls-FORWARD_and_NAT_Rules.html

## Enable services


    sudo systemctl enable --now nftables
    sudo systemctl enable --now nginx
    sudo systemctl enable --now dhcpd

