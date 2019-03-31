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
auth = firebase.auth()
db = firebase.database()
users = db.child("Users")

@app.route("/enhance", methods=["POST"])
def enhance():
    if request.method == 'POST':
        content = request.json

       
        
            #user = auth.sign_in_with_custom_token(token)
        userId = content["userId"]
        accessToken = content['accessToken']
        
        userToken = users.child(userId).child("accessToken").get().val()
        if accessToken == userToken:


        
        
            imageString = content['imageString']
            imageData = base64.b64decode(imageString) 
    ####
    #### Add machine learning model code here
    ####

            return jsonify({"imageData" : str(imageData)})
        else:
            return jsonify({"error": "incorrect access token"})
     


@app.route("/token", methods=["POST"])
def token():
    if request.method == 'POST':
        content = request.json

        uid = content['uid']

        token = auth.create_custom_token("your_custom_id")

        return(jsonify({'token': token}))
