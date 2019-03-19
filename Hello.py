'''
Created on 19 mar 2019

@author: mpasteri

http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
'''

from flask import Flask


appMax = Flask(__name__)

@appMax.route("/")
def home():
    return "Ciaooo da Massimo"

if __name__ == "__main__":
    appMax.run(debug=True)    
