from flask import Flask, render_template, request
from datetime import datetime
from urllib.parse import urlparse
import requests
from requests.auth import HTTPBasicAuth
import hashlib
import re
import os
import ipaddress
import json
import subprocess

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

knet_api_base_url = "https://api.k-net.dk/v2/"

# HTTP / HTTPS login site and hostname
captive_scheme = "https"
captive_hostname = "captive.pop.dk"
# Semi-hardcoded configuration variables - END


# Get API username and password from environment variables
knet_api_username = os.environ.get("KNET_API_USERNAME")
knet_api_password = os.environ.get("KNET_API_PASSWORD")

app = Flask(__name__)

# now in template: https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Get current state, who is logged in? This is defined by what interfaces that are open
# TODO: Cache result for request
def get_open_interfaces():
    # Get the list of open interfaces from nft
    result_raw = subprocess.run(['/usr/bin/sudo', '/usr/sbin/nft', '-j', 'list', 'set', 'ip', 'captive', 'open_interfaces'], stdout=subprocess.PIPE)

    # Get the output and decode it
    result_json = json.loads(result_raw.stdout)

    # Prepare list for open interfaces
    open_interfaces = []

    # Extract the interface names for the open interfaces
    for element in result_json['nftables'][1]['set']['elem']:
        open_interfaces.append(element['elem']['val'])

    return open_interfaces

# Get interface for current request
# TODO: Cache result for request
def get_current_interface():
    # TODO: Use https://docs.python.org/3/library/ipaddress.html instead of regex here
    # If we are here we have a valid login. Let us open the internet!
    # Check what vlan we are on from the IP address 172.16.2xx.yyy
    # We need to capture xx as this is the index for that vlan in our settings.py
    # yyy is not important. Any device on that network (vlan) can login
    # yyy must be between 0 and 255, ensured by this regex.
    # X-Real-IP is because of proxy. This application will always use the same proxy so no need to check anything else
    pattern = re.compile(r'^172\.16\.2([0-9]{2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]|[0-9])$')
    match_ip_to_interface = int(pattern.match(request.headers['X-Real-IP']).group(1))

    # Check valid interface number
    if match_ip_to_interface < 0 or match_ip_to_interface >= len(interfaces):
        # Reject because of invalid interface id
        return render_template('public-ip.html')

    # Current interface is:
    return interfaces[match_ip_to_interface]

# Check if logged in already
def is_current_interface_logged_in():
    # Get current list of open interfaces
    open_interfaces = get_open_interfaces()

    # Get current interface name
    current_interface = get_current_interface()

    # If current_interface is in the list of open interfaces the current interface is logged in
    if current_interface in open_interfaces:
        return True

    # If not, then nobody is logged in
    return False


# TODO: Do not send 511 if user is logged in
# X-Real-IP is because of proxy. This application will always use the same proxy so no need to check anything else
@app.before_request
def before_request():
    # Check for private IP. Only show captive portal on the inside of our network
    if ipaddress.ip_address(request.headers['X-Real-IP']).is_private == False:
        return render_template('public-ip.html')

    # Check hostname. If wrong send 511 for login required
    o = urlparse(request.base_url)
    host = o.hostname
    if o.hostname != captive_hostname:
        # Only send 511 if interface is not logged in.
        if is_current_interface_logged_in() == False:
            return render_template('login-required-redirect.html',
                redirect_host=captive_scheme + "://" + captive_hostname + "/"), 511

        # Otherwise return a normal 404
        abort(404)


# Show login form
@app.route('/', methods=['GET'])
def show_login_logout():
    # Offer logout if interface is logged in
    if is_current_interface_logged_in():
        return render_template('logout.html',
            title="Captive portal - Log ud"
            )

    # Otherwise interface is not yet logged in, Offer login
    return render_template('login.html',
        title="Captive portal - Log ind"
        )

# Perform login
@app.route('/login', methods=['POST'])
def login_now():
    username = request.form.get('username')
    password = request.form.get('password')
    accept_tos = request.form.get('accept_tos')

    # Check that terms and conditions (Terms of Service - ToC) has been accepted
    if accept_tos != 'on':
        return render_template('invalid-login.html',
            title="Captive portal - Log ind mislykkedes Kode:#666",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Check login with K-Net API, reject if invalid.
    user_response = requests.get(
        knet_api_base_url + 'network/user/?username=' + username, 
        auth=HTTPBasicAuth(knet_api_username, knet_api_password)
    )

    # Check if we got a 200 OK
    # If not we cannot check the login and we should fail right here
    if user_response.status_code != 200:
        return render_template('invalid-login.html',
            title="Captive portal - Log ind mislykkedes Kode:#1",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # There should only be one response.
    # If less then no user was found.
    # If more then we cannot check password correctly.
    # TODO Handle lack of ['count'] key in a graceful way
    if user_response.json()['count'] != 1:
        return render_template('invalid-login.html',
            title="Captive portal - Log ind mislykkedes Kode:#2",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Get password to compare. First result contain password with salt
    password_from_knet = user_response.json()['results'][0]['password']

    # Get the password parts. Format should be sha1$[SALT]$[HASH]
    pwd_parts = password_from_knet.split('$')

    # We check that sha1 was used. If not we cannot check the password
    if pwd_parts[0] != 'sha1':
        return render_template('invalid-login.html',
            title="Captive portal - Log ind mislykkedes Kode:#3",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Perform the hashing with the given password and the salt from k-net
    hash_result = hashlib.sha1(bytes(pwd_parts[1]+password, 'utf-8')).hexdigest()

    # Check aginst the salt+hash stored at K-Net
    # If not OK: Stop here
    if hash_result != pwd_parts[2]:
        # Reject if login is invalid
        return render_template('invalid-login.html',
            title="Captive portal - Log ind mislykkedes Kode:#4",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Inteface to open is:
    interface_to_open = get_current_interface()

    # Make string to save in log file username + vlan id?
    # TODO Add timezone to timestamp. For now it is as system time
    save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + username + "," + interface_to_open + "," + request.headers['X-Real-IP'] + "," + user_response.json()['results'][0]['vlan'] + "\n"

    # Save this string to log file
    log_file_path = '/var/log/pop-captive/'
    current_date = datetime.now().strftime("%Y%m%d")
    log_filename = 'pop-captive-access-' + current_date + '.log'
    log_file = open(log_file_path + log_filename, 'a')
    log_file.write(save_to_log)
    log_file.close()

    # TODO Read log again to be sure it was written correctly

    # Call nft command with sudo to open that network
    cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'add element captive open_interfaces { " + interface_to_open + " }'")
    if os.WEXITSTATUS(cmd) != 0:
        # Show failure if cmd to open interface did not work
        return render_template('invalid-login.html',
            title="Captive portal - Log ind ok, kunne ikke give adgang til internet Code:#6 ",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Show success message for login, redirect to https://pop.dk/
    return render_template('valid-login-redirect.html',
        title="Captive portal - Log ind accepteret"
        )

# Perform logout
@app.route('/logout', methods=['POST'])
def logout_now():
    # Inteface to close is:
    interface_to_close = get_current_interface()

    # Make string to save in log file username + vlan id?
    # TODO Add timezone to timestamp. For now it is as system time
    save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",system_close_on_logout_request," + interface_to_close + "," + request.headers['X-Real-IP'] + ",\n"

    # Save this string to log file
    log_file_path = '/var/log/pop-captive/'
    current_date = datetime.now().strftime("%Y%m%d")
    log_filename = 'pop-captive-access-' + current_date + '.log'
    log_file = open(log_file_path + log_filename, 'a')
    log_file.write(save_to_log)
    log_file.close()

    # TODO Read log again to be sure it was written correctly

    # Call nft command with sudo to open that network
    cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'delete element captive open_interfaces { " + interface_to_close + " }'")
    if os.WEXITSTATUS(cmd) != 0:
        # Show failure if cmd to open interface did not work
        return render_template('error-logout.html',
            title="Captive portal - Log ud mislykkedes ",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Show success message for login, redirect to https://pop.dk/
    return render_template('valid-logout.html',
        title="Captive portal - Log ud accepteret",
            login_link=captive_scheme + "://" + captive_hostname + "/"
        )
