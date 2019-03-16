class Users:
    def __init__(self):
        self.users = []

    def get_all_users(self):
        return self.users

    def add_user(self, user):
        return self.users.append(user)

class User:
    def __init__(self, email, firstname, lastname, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def signup(self):
        return {"email": self.email, "firstname": self.firstname, 
            "lastname": self.lastname, "password": self.password}