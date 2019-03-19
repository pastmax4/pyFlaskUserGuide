'''
Created on 19 mar 2019

@author: mpasteri

http://flask.pocoo.org/docs/1.0/quickstart/#routing

'''
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Questo is un POST"
    else:
        return "Questo  is not un POST."

#-------------------------------------------------------------
#-------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)    

