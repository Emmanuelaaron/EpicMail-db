from tests.test_base import BaseTest
from flask import json
from api import app

class Test_messages(BaseTest):
    def test_send_email(self):
        self.user = {
            "email": "alexander@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.user2 = {
            "email": "violet@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.message = {
            "subject": "people",
	        "message": "blah blah, blaha",
	        "receiver_id": 1
        }
        self.signup_user(self.user)
        self.signup_user(self.user2)
        login = self.login_user({
                "email": "alexander@gmail.com",
                "password": "12345"
            })
        resp = app.test_client(self).post("api/v1/messages",
                headers={"x-access-token": login},
                content_type="application/json", data=json.dumps(self.message)
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(reply["message"], "message sent")

    def test_send_email_with_receiver_not_existin(self):
        self.user = {
            "email": "bernard@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.message = {
            "subject": "people",
	        "message": "blah blah, blaha",
	        "receiver_id": 4787878
        }
        self.signup_user(self.user)
        login = self.login_user({
                "email": "bernard@gmail.com",
                "password": "12345"
            })
        resp = app.test_client(self).post("api/v1/messages",
                headers={"x-access-token": login},
                content_type="application/json", data=json.dumps(self.message)
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(reply["message"], "Oops... Reciever does not exist on this app")

    def test_send_email_with_empty_fields(self):
        self.user = {
            "email": "ronaldo@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.message = {
            "subject": "  ",
	        "message": "blah blah",
	        "receiver_id": 4
        }
        self.signup_user(self.user)
        login = self.login_user({
                "email": "ronaldo@gmail.com",
                "password": "12345"
            })
        resp = app.test_client(self).post("api/v1/messages",
                headers={"x-access-token": login},
                content_type="application/json", data=json.dumps(self.message)
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 400)
        self.assertIn("All fields must be filled", str(reply))

    def test_get_all_email(self):
        self.user = {
            "email": "jason@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.signup_user(self.user)
        login = self.login_user({
                "email": "jason@gmail.com",
                "password": "12345"
            })
        resp = app.test_client(self).get("api/v1/messages",
                headers={"x-access-token": login},
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertIn("'Oops..you do not have any messages!", str(reply))
        
    def test_get_specific_email(self):
        self.user = {
            "email": "precious@gmail.com",
          
    def test_get_sent_emails(self):
        self.user = {
            "email": "resty@gmail.com",
          
    def test_delete_email(self):
        self.user = {
            "email": "arnold@gmail.com",
            "firstname": "sonibil",
            "lastname": "kironde",
            "password": "12345"
        }
        self.signup_user(self.user)
        login = self.login_user({
            "email": "precious@gmail",
            "password": "12345"
        })
        resp = app.test_client(self).get("api/v1/messages/7878",
                headers={"x-access-token": login})
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
                "email": "resty@gmail.com",
                "password": "12345"
            })
        resp = app.test_client(self).get("api/v1/messages/sent",
                headers={"x-access-token": login},
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Oops.. you don't have any sent messages!", str(reply))
 
            "email": "arnold@gmail.com",
            "password": "12345"
        })
        resp = app.test_client(self).delete("api/v1/messages/1",
            headers={"x-access-token": login}
            )
        reply = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
