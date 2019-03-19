'''
Created on 19 mar 2019

@author: mpasteri

http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
'''

from flask import Flask


appMax = Flask(__name__)

#-------------------------------------------------------------
@appMax.route("/")
def home():
    return "Questa is una prova dalla user guide di Flask. "

#-------------------------------------------------------------
#Questa is la URL:
#http://127.0.0.1:5000/hello
@appMax.route('/hello')
def hello():
    return 'Hello World from Massimo.'

#-------------------------------------------------------------
#Nota che ora c e lo slash finale.
@appMax.route('/projects/')
def projects():
    return 'The project page'


#-------------------------------------------------------------
#-------------------------------------------------------------
if __name__ == "__main__":
    appMax.run(debug=True)    

