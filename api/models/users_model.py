class Users:
    def __init__(self):
        self.users = []

    def get_all_users(self):
        return self.users

    def add_user(self, user):
        self.users.append(user)

    def find_user_by_id(self, user_id):
        user = [user for user in self.users if user["user_id"] == user_id]
        return user

    def find_user_id_by_email(self, email):
        user_id = [user["user_id"] for user in self.users if user["email"] == email]
        return user_id

class User:
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def signup(self):
        return {"email": self.email, "firstname": self.firstname, 
            "lastname": self.lastname, "password": self.password}