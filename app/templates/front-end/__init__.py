#import urllib2
from flask import Flask, render_template, request, session, redirect, url_for
import json


app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    return 'Hello, World!'


if __name__=="__main__":
    app.debug = True
    app.run()