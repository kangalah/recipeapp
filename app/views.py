
from flask import render_template,request
from app.___init__ import app 

@app.route('/')
def index():
    return render_template('index.html') 