import unittest
from api import app
from flask import json
# import jwt

class BaseTest(unittest.TestCase):
    def setup(self):
        self.tester = app.test_client(self)
        self.user = {
            "email": "emmanuel@gmail.com",
            "firstname": "emmanuel",
            "lastname": "isabirye",
            "password": "12323q"
        }

        self.signup_user(self.user)


    def signup_user(self, user):
        signedup_user = app.test_client(self).post("/api/v1/auth/signup", 
        content_type="application/json", data=json.dumps(user))
        return signedup_user

    def login_user(self, user):
        loggedin_user = app.test_client(self).post("api/v1/auth/login",
        content_type="application/json", data=json.dumps(user))
        token = json.loads(loggedin_user.data.decode())
        return token["token"]

