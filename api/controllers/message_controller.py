from flask import request, jsonify
from api.models.message_model import Message, Messages
from api.validators import Validators
from api.controllers.users_controllers import user_list
from api.token.jwt_token import authenticate

auth = authenticate()
validator = Validators()
messages = Messages()

class Decoder:
    @staticmethod
    def decoded_token():
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        decoded = auth.decode_auth_token(token)
        return decoded
        

class message_controller():

    def send_email(self):
        data = request.get_json()
        subject = data.get("subject")
        message = data.get("message")
        receiver_id = data.get("receiver_id")

        info = [subject, message]
        sender_email = Decoder.decoded_token()
        sender_id = user_list.find_user_id_by_email(sender_email)[0]
        if receiver_id == sender_id:
            return jsonify({
                "message": "You can't send a message to your self"
            })
        for detail in info:
            if detail.isspace() or len(detail) == 0:
                return jsonify({"missing": "All fields must be filled"})
        if len(user_list.get_all_users()) == 0:
            return jsonify({
                "message": "Oops No one is signedup for this email"
            })
        new_user = user_list.find_user_by_id(receiver_id)
        if new_user:
            my_message = Message(subject, message)
            my_message = my_message.create_message()
            my_message["message_id"] = len(messages.get_all_messages()) + 1
            my_message["receiver_id"] = receiver_id
            my_message["sender_id"] = sender_id
            messages.add_message(my_message)
            return jsonify({"message": "message sent"})
        return jsonify({"message": "Oops... Reciever does not exist on this app"})
           