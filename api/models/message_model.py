import datetime

class Messages():
    def __init__(self):
        self.messages = []

    def add_message(self, email):
        return self.messages.append(email)

    def get_all_messages(self):
            return self.messages

    def get_all_received_messages_by_user_id(self, user_id):
        messages = [message for message in self.messages if message["receiver_id"] == user_id]
        return messages

    def get_all_messages_by_user_id(self, user_id):
        messages = [message for message in self.messages if message["receiver_id"] == user_id or message["sender_id"] == user_id]
        return messages

    def get_message_with_specific_message_id(self, message_id):
        message = [message for message in self.messages if message["message_id"] == message_id]
        return message
class Message():
    
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message


    def create_message(self):
        return {
            "subject": self.subject,
            "message": self.message,
            "status": "draft",
            "createdOn":  datetime.date.today()

        }

