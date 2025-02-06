from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager
from wtforms import FormField

# Initialize the Flask app
app = Flask(__name__)

# Configure a secret key for security purposes
app.secret_key = 'your-secret-key-here'

# Create a login manager instance
login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)