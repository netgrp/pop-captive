from flask import Flask, render_template, request
from datetime import datetime
from urllib.parse import urlparse
import requests
from requests.auth import HTTPBasicAuth
import hashlib
import re

app = Flask(__name__)

# now in template: https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Check hostname. If wrong send 511 for login required
# TODO: Do not send 511 if user is logged in
# TODO: Not hardcode captive.pop.dk
@app.before_request
def before_request():
    o = urlparse(request.base_url)
    host = o.hostname
    if o.hostname != 'captive.pop.dk':
        return render_template('login-required-redirect.html'), 511


# Show login form
@app.route('/', methods=['GET'])
def show_login():
    return render_template('login.html',
        title="Captive portal login"
        )

# Perform login
@app.route('/', methods=['POST'])
def login_now():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check login with K-Net API, reject if invalid.
    user_response = requests.get(
        knet_api_base_url + 'network/user/?username=' + username, 
        auth=HTTPBasicAuth(knet_api_username, knet_api_password)
    )

    # There should only be one response.
    # If less then no user was found.
    # If more then we cannot check password correctly.
    if user_response.json()['count'] != 1:
        return render_template('invalid-login.html',
            title="Captive portal login failed"
            )

    # Get password to compare. First result contain password with salt
    password_from_knet = user_response.json()['results'][0]['password']

    # Get the password parts. Format should be sha1$[SALT]$[HASH]
    pwd_parts = password_from_knet.split('$')

    # We check that sha1 was used. If not we cannot check the password
    if pwd_parts[0] != 'sha1':
        return render_template('invalid-login.html',
            title="Captive portal login failed"
            )

    # Perform the hashing with the given password and the salt from k-net
    hash_result = sha1(bytes(pwd_parts[1]+password, 'utf-8')).hexdigest()

    # Check aginst the salt+hash stored at K-Net
    # If not OK: Stop here
    if hash_result != pwd_parts[2]:
        # Reject if login is invalid
        return render_template('invalid-login.html',
            title="Captive portal login failed"
            )

    # If we are here we have a valid login. Let us open the internet!
    # Check what vlan we are on from the IP address 172.16.2xx.yyy
    # We need to capture xx as this is the index for that vlan in our settings.py
    # yyy is not important. Any device on that network (vlan) can login
    # yyy must be between 0 and 255, ensured by this regex.
    pattern = re.compile(r'^172\.16\.2([0-9]{2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]|[0-9])$')
    match_ip_to_interface = int(pattern.match(request.remote_addr).group(1))

    # Check valid interface number
    if match_ip_to_interface < 0 or match_ip_to_interface >= len(interfaces):
        # Reject because of invalid interface id
        return render_template('invalid-login.html',
            title="Captive portal login failed"
            )

    # Inteface to open is:
    interface_to_open = interfaces[match_ip_to_interface]

    # Make string to save in log file username + vlan id?
    # TODO Add timezone to timestamp. For now it is as system time
    save_to_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + username + "," + interface_to_open + "," + request.remote_addr + "," + user_response.json()['results'][0]['vlan']

    # Save this string to log file
    log_file = open('/var/log/pop-captive-access.log', 'a')
    log_file.write(save_to_log)
    log_file.close()

    # TODO Read log again to be sure it was written correctly
    # Call nft command with sudo to open that network
    os.system("nft 'add element captive open_interfaces { " + interface_to_open + " }'")

    # Show success message for login, redirect to https://pop.dk/
    return render_template('valid-login-redirect.html',
        title="Captive portal login accepted"
        )
