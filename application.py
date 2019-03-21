'''
Created on 21 mar 2019

@author: mpasteri

http://flask.pocoo.org/docs/1.0/quickstart/#routing

I file di questa app sono nella dir templateRendering.
In realta la dir si deve chiamare templates infatti:
Flask will look for templates in the templates folder. 
So if your application is a module, this folder is next to that module, 
if it’s a package it’s actually inside your package:
/application.py
/templates
    /hello.html
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#-------------------------------------------------------------
#-------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)    
