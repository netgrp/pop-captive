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
* cron - To delete old logs via a cron job

To install this in Fedora. We do not want firewalld

    sudo dnf mark install nftables
    sudo dnf remove firewalld
    sudo dnf install dhcp nginx certbot certbot-nginx git python3-virtualenv cronie

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
    sudo systemctl enable --now crond.service

## Set environment variables (Should be possible in the .service file for Gunicorn 3)

    KNET_API_USERNAME=
    KNET_API_PASSWORD=


https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-environment-variables

## Make user for pop-captive flask application

    $ sudo useradd pop-captive

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

VERY IMPORTANT: Remember to add K-Net API Username and Password to the environment variables in the service file!

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

## Prepare log file for use

    $ sudo mkdir -p /var/log/pop-captive
    $ sudo chown -R pop-captive:pop-captive /var/log/pop-captive/

## Setup job to delete old logs for legal and practical reasons (run as root)

Remember to make script executeable

    $ sudo su
    # echo "0 4 * * * pop-captive /opt/pop-captive/scripts/remove-old-logs.sh" >> /etc/crontab
    # chmod +x /opt/pop-captive/scripts/remove-old-logs.sh

## Allow captive portal to open the internet

Edit the /etc/sudoers file. See the configuration-service/sudoers.md file for how to do this. We allow it to use sudo for specific commands without password

## For debugging, follow the logs. Python errors will show up here.

    $ journalctl -f

## TODO


Future work, improvments waiting to be implemented after some testing

* Let web portal be aware of active networks:
  * Automatic log out if device disconnected. Send ARP requests every 1 minute and log user out if no response in some given time.
* Gracefull error handeling
  * Do not leak error codes in the same way as now
  * Handle missing keys such as ['count'] in a gracefull manner
  * Catch errors in a more general manner (send e-mail?)
* Log files
  * Gunicorn logs save in a easy to access way with logrotate if required
  * Logrotate on any log this application generates!
  * Save info that can be used for debugging for normal errors to help users.
* User experience: Redirect to intended page instead of https://pop.dk/
  * e.g. http://detectportal.firefox.com/success.txt
* Hardening of nginx configuraiton
  * HSTS
  * Hide nginx version
  * Rate limit in nginx
  * Deny common extensions not used
  * Inspiration: kakaomaelk and pf
  * Customized error pages to hide what layer that fail (Error page looks different in Flask and Nginx right now)
  * Get A+ on https://www.ssllabs.com/ssltest/analyze.html?d=captive.pop.dk
  * Be sure to check out: https://docs.gunicorn.org/en/stable/deploy.html
* More complete instructions for nginx setup, including HTTPS setup.
* Heartbeat url for status.pop.dk: Say OK if everything seems to work as it should
* Make it possible to show terms and conditions when logged in
