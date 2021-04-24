from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# now in template: https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template

@app.route('/')
def hello_world():
    return render_template('pop-template.html',
        title="Captive portal, Eksempel titel",
        content="Eksempel indhold",
        now=datetime.utcnow()
        )
