from flask import Flask
from flask import request
from flask import jsonify
import base64
import pyrebase

app = Flask(__name__)

config = {
    "apiKey"            : "AIzaSyDdI7_URyohA97SrSTtZIwfDG5YjtRpL4U",
    "authDomain"        : "unscrambleai.firebaseapp.com",
    "databaseURL"       : "https://unscrambleai.firebaseio.com",
    "projectId"         : "unscrambleai",
    "storageBucket"     : "unscrambleai.appspot.com",
    "messagingSenderId" : "1064084272987"
}
firebase = pyrebase.initialize_app(config)

@app.route("/enhance", methods["POST"])
def enhance():
    if request.method == 'POST':
        content = request.json

        token = content['token']
        try:
            user = auth.sign_in_with_custom_token(token)
        
            imageString = content['imageString']
            imageData = base64.b64decode(imageString)

        ####
        #### Add machine learning model code here
        ####

            results = {"imageData" : "<some-base64-string>"}
            return jsonify(results)
        except:
            return jsonify({"error"})


