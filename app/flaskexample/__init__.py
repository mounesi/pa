# initialization
#creates the application object (of class Flask), 
#which we have called app, and then 
#imports the views module, which we haven't written yet. 
#The views are the handlers that respond to requests from web browsers

from flask import Flask
app = Flask(__name__)
from flaskexample import views
