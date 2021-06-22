###########################
## Environment Variables ##                                              
###########################

import ast
import os

# os.chdir(os.getcwd() + "/my_backend_test/src")
print(os.getcwd())

##############
## Back-End ##                                              
##############

## Flask Endpoints, Swagger Etc.
from flask import Flask, g, request, send_from_directory, abort, request_started, jsonify

from flask_cors import CORS ## Cross-origin resource sharing (CORS);
                            ## some endpoint related story check at it online.

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import Api, swagger
from flask_json import FlaskJSON, json_response

##########################
## App - Initialization ##
##########################

app = Flask(__name__)

CORS(app)       ## add-in. see above.
FlaskJSON(app)  ## simply adds better JSON support to Flask
                ## application.

########################
## App Configuration  ##
########################

from app.config import Config

# Configuration
app.config.from_object(Config)

##########################
## DB for flask alchemy ##
##########################

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#################
## Flask-login ##
#################

from flask_login import LoginManager

login = LoginManager(app)
login.login_view = 'login' # tells flask which one the log in function is. Like this you redirect to the login page if not already logged in.

from app import routes

## Run the application
if __name__ == "__main__":
    print("here")
    app.run(debug=True)
