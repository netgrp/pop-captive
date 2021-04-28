from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# now in template: https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Åbne for dhcp i firewall - husk at gøre det pr zone frem for alt!
# sudo firewall-cmd --add-service=dhcp --permanent

# TODO: firewall rules for server in general now that fwdaemon was removed

# That 511 error code reponse


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

    # Reject if login is invalud

    # Find what kitchen

    # Make string to save in log file

    # Save this string to log file
    # Read it again to be sure it is there
    # Call nft command with sudo to open that network
    # Show success message for login, redirect to https://pop.dk/
    return render_template('invalid-login.html',
        title="Captive portal login failed"
        )
