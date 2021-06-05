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
* Gunicon - WSGI middle layer between nginx and flask. Used to deploy flask in production. Via pip for virtualenv to work correctly
* Certbot - and certbot plugin for nginx for SSL certificate to make https work
* git - to download the appliaction and install updates easier
* virtualenv - For the python flask application, to keep them in a "container".

To install this in Fedora. We do not want firewalld

    sudo dnf mark install nftables
    sudo dnf remove firewalld
    sudo dnf install dhcp nginx certbot certbot-nginx git python3-virtualenv

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
    sudo systemctl enable --now certbot-renew.timer

## Set environment variables (Should be possible in the .service file for Gunicorn 3)

    KNET_API_USERNAME=
    KNET_API_PASSWORD=


https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-environment-variables

## Make user for pop-captive flask application

    $ sudo useradd pop-captive
    $ sudo usermod -aG wheel pop-captive

## Getting the base files right

    $ sudo mkdir -p /opt/pop-captive/
    $ sudo chown -R pop-captive:pop-captive /opt/pop-captive/
    $ cd /opt/pop-captive/
    $ sudo su pop-captive
    $ git clone https://github.com/eKristensen/pop-captive.git /opt/pop-captive

## Prepare virtual environment (still as the pop-captive user) and install python packages (this includes flask, gunicorn)

    $ virtualenv pop-captive-venv
    $ source pop-captive-venv/bin/activate
    $ pip install -r requirements.txt

## Install service file for Gunicorn. Run as normal user with sudo rights

    $ sudo cp /opt/pop-captive/configuration-services/pop-captive.service /etc/systemd/system/pop-captive.service
    $ sudo systemctl enable --now pop-captive

## Fix SELinux if required. It may block starting Gunicorn (permissiond denied error, confirm here with `ausearch -m avc -ts recent`)

This includes the policy required in order to allow nginx to access the socket for Gunicorn.

    $ sudo restorecon -R -v /opt/pop-captive/
    $ cd /opt/pop-captive/configuration-services/
    $ sudo semodule -i pop-captive.pp

Relevant websites for SELinux:
* https://command-not-found.com/audit2allow
* https://docs.fedoraproject.org/en-US/Fedora/12/html/Security-Enhanced_Linux/sect-Security-Enhanced_Linux-Fixing_Problems-Allowing_Access_audit2allow.html
* https://wiki.gentoo.org/wiki/SELinux/Tutorials/Creating_your_own_policy_module_file

## Activate HTTPS with certbot

    $ sudo certbot renew
