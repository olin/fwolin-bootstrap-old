import os, random, string, requests, json, re, time, fwolin
from flask import Flask, session, request, redirect, url_for, render_template

# Initialize Flask application.
app = Flask(__name__, static_url_path='')

# Use fwol.in's unified authentication mechanism.
# This requires us to set an environment variable for this application
# to encrypt the user's session.
fwolin.enable_auth(app)
Flask.secret_key = os.environ.get('FLASK_SESSION_KEY', 'test-key-please-ignore')

# Routes
# ------

@app.route('/')
def index():
	return render_template('index.html', email=session['email'])

# Launch
# ------

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    if 'PORT' in os.environ:
    	app.config.update(SERVER_NAME='fwol.in')
    app.run(host='0.0.0.0', port=port)
