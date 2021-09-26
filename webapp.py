from flask import Flask, render_template, request, abort
from datetime import datetime
from urllib.parse import urlparse
import requests
from requests.auth import HTTPBasicAuth
import hashlib
import re
import os
import ipaddress
from common import get_logged_in_ips

knet_api_base_url = "https://api.k-net.dk/v2/"

# HTTP / HTTPS login site and hostname
captive_scheme = "https"
captive_hostname = "lan.pop.dk"
# Semi-hardcoded configuration variables - END


# Get API username and password from environment variables
knet_api_username = os.environ.get("KNET_API_USERNAME")
knet_api_password = os.environ.get("KNET_API_PASSWORD")

app = Flask(__name__)

# now in template: https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Check if logged in already
# Check by IP
def is_ip_logged_in(ip_to_check):
    # If current ip is in the list of open ips the current ip is logged in
    if ip_to_check in get_logged_in_ips():
        return True

    # If not, then nobody is logged in
    return False


# TODO: Do not send 511 if user is logged in
# X-Real-IP is because of proxy. This application will always use the same proxy so no need to check anything else
@app.before_request
def before_request():
    # Check for private IP. Only show Lan captive portal on the inside of our network
    if ipaddress.ip_address(request.headers['X-Real-IP']).is_private == False:
        return render_template('public-ip.html')

    # Check hostname. If wrong send 511 for login required
    o = urlparse(request.base_url)
    host = o.hostname
    if o.hostname != captive_hostname:
        # Only send 511 if interface is not logged in.
        if is_ip_logged_in(request.headers['X-Real-IP']) == False:
            return render_template('login-required-redirect.html',
                redirect_host=captive_scheme + "://" + captive_hostname + "/"), 511

        # Otherwise return a normal 404
        abort(404)


# Show login form
@app.route('/', methods=['GET'])
def show_login_logout():
    # Offer logout if interface is logged in
    if is_ip_logged_in(request.headers['X-Real-IP']):
        return render_template('logout.html',
            title="Lan captive portal - Log ud"
            )

    # Otherwise interface is not yet logged in, Offer login
    return render_template('login.html',
        title="Lan captive portal - Log ind"
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
            title="Lan captive portal - Log ind mislykkedes Kode:#666",
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
            title="Lan captive portal - Log ind mislykkedes Kode:#1",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # There should only be one response.
    # If less then no user was found.
    # If more then we cannot check password correctly.
    # TODO Handle lack of ['count'] key in a graceful way
    if user_response.json()['count'] != 1:
        return render_template('invalid-login.html',
            title="Lan captive portal - Log ind mislykkedes Kode:#2",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Get password to compare. First result contain password with salt
    password_from_knet = user_response.json()['results'][0]['password']

    # Get the password parts. Format should be sha1$[SALT]$[HASH]
    pwd_parts = password_from_knet.split('$')

    # We check that sha1 was used. If not we cannot check the password
    if pwd_parts[0] != 'sha1':
        return render_template('invalid-login.html',
            title="Lan captive portal - Log ind mislykkedes Kode:#3",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Perform the hashing with the given password and the salt from k-net
    hash_result = hashlib.sha1(bytes(pwd_parts[1]+password, 'utf-8')).hexdigest()

    # Check aginst the salt+hash stored at K-Net
    # If not OK: Stop here
    if hash_result != pwd_parts[2]:
        # Reject if login is invalid
        return render_template('invalid-login.html',
            title="Lan captive portal - Log ind mislykkedes Kode:#4",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Make string to save in log file username + vlan id?
    # TODO Add timezone to timestamp. For now it is as system time
    save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + username + ",lan_party," + request.headers['X-Real-IP'] + "," + user_response.json()['results'][0]['vlan'] + "\n"

    # Save this string to log file
    log_file_path = '/var/log/pop-captive/'
    current_date = datetime.now().strftime("%Y%m%d")
    log_filename = 'pop-captive-access-' + current_date + '.log'
    log_file = open(log_file_path + log_filename, 'a')
    log_file.write(save_to_log)
    log_file.close()

    # TODO Read log again to be sure it was written correctly

    # Call nft command with sudo to open that network
    cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'add element captive open_ips_lan_party { " + request.headers['X-Real-IP'] + " }'")
    if os.WEXITSTATUS(cmd) != 0:
        # TODO: Also add this failure to the log
        # Show failure if cmd to open interface did not work
        return render_template('invalid-login.html',
            title="Lan captive portal - Log ind ok, kunne ikke give adgang til internet Code:#6 ",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Show success message for login, redirect to https://pop.dk/
    return render_template('valid-login-redirect.html',
        title="Lan captive portal - Log ind accepteret"
        )

# Perform logout
@app.route('/logout', methods=['POST'])
def logout_now():
    # Make string to save in log file username + vlan id?
    # TODO Add timezone to timestamp. For now it is as system time
    save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",system_close_on_logout_request,lan_party," + request.headers['X-Real-IP'] + ",\n"

    # Save this string to log file
    log_file_path = '/var/log/pop-captive/'
    current_date = datetime.now().strftime("%Y%m%d")
    log_filename = 'pop-captive-access-' + current_date + '.log'
    log_file = open(log_file_path + log_filename, 'a')
    log_file.write(save_to_log)
    log_file.close()

    # TODO Read log again to be sure it was written correctly

    # Call nft command with sudo to open that network
    cmd = os.system("/usr/bin/sudo /usr/sbin/nft 'delete element captive open_ips_lan_party { " + request.headers['X-Real-IP'] + " }'")
    if os.WEXITSTATUS(cmd) != 0:
        # TODO: Also add this failure to the log
        # Show failure if cmd to open interface did not work
        return render_template('error-logout.html',
            title="Lan captive portal - Log ud mislykkedes ",
            retry_link=captive_scheme + "://" + captive_hostname + "/"
            )

    # Show success message for login, redirect to https://pop.dk/
    return render_template('valid-logout.html',
        title="Lan captive portal - Log ud accepteret",
            login_link=captive_scheme + "://" + captive_hostname + "/"
        )
