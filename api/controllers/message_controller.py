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
            }), 400
        for detail in info:
            if detail.isspace() or len(detail) == 0:
                return jsonify({"missing": "All fields must be filled"}), 400
        if len(user_list.get_all_users()) == 0:
            return jsonify({
                "message": "Oops No one is signedup for this email"
            })
        new_user = user_list.find_user_by_id(receiver_id)
        if new_user:
            my_message = Message(subject, message)
            new_message = my_message.create_message()
            new_message["message_id"] = len(messages.get_all_messages()) + 1
            new_message["receiver_id"] = receiver_id
            new_message["sender_id"] = sender_id
            messages.add_message(new_message)
            return jsonify({"message": "message sent"}), 201
        return jsonify({"message": "Oops... Reciever does not exist on this app"})

    def get_all_received_emails(self):
        receiver_email = Decoder.decoded_token()
        if len(user_list.find_user_id_by_email(receiver_email)) == 0:
            return jsonify({
                "message": "You do not have an account here! Please signup"
            })
        receiver_id = user_list.find_user_id_by_email(receiver_email)[0]
        inbox_messages = messages.get_all_received_messages_by_user_id(receiver_id)
        if not inbox_messages:
            return jsonify({
                "status": 200,
                "message": "Oops..you do not have any messages!"
            }), 200
        return jsonify({
            "status": 200,
            "data": inbox_messages
        }), 200
      
    def get_sent_emails(self):
        sender_email = Decoder.decoded_token()
        if len(user_list.find_user_id_by_email(sender_email)) == 0:
            return jsonify({
                "message": "You do not have an account here! Please signup"
            })
        send_id = user_list.find_user_id_by_email(sender_email)[0]
        sent_messages = messages.get_all_sent_messages_by_user_id(send_id)
        if not sent_messages:
            return jsonify({
                "status": 200,
                "message": "Oops.. you don't have any sent messages!"
            }), 200
        return jsonify({
            "status": 200,
            "data": sent_messages
        })
      
    def delete_specific_email(self, message_id):
        user_email = Decoder.decoded_token()
        user_id = user_list.find_user_id_by_email(user_email)[0]
        messages_ = messages.get_all_messages_by_user_id(user_id)
        if not messages_:
            return jsonify({
                "message": "You have no sent or received messages!"
            })
        to_be_deleted = messages.get_message_with_specific_message_id(message_id)
        if not to_be_deleted:
            return jsonify({
                "message": "Message with that id does not exist among your emails"
            })
        messages.get_all_messages().remove(to_be_deleted[0])
        return jsonify({
            "message": "you've sucessfully deleted the message"
        }), 200

