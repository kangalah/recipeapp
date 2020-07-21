from . import app
from flask import render_template

@app.route('/')
def register():
    return render_template('register.html')