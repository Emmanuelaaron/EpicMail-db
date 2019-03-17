from api.models.users_model import User, Users
from flask import jsonify, request
from api.validators import Validators
from api.jwt_token import encode_auth_token

user_list = Users()
Validator = Validators()
class UsersController:

    def signup_user(self):
        try:
            data = request.get_json()
            email = data.get("email")
            firstname = data.get("firstname")
            lastname = data.get("lastname")
            password = data.get("password")

            user_details = [email, firstname, lastname, password]
            errors = Validator.validate(user_details, email)
            if len(errors) > 0:
                return jsonify({"errors": errors}), 400
            for user in user_list.get_all_users():
                if user["email"] == email:
                    return jsonify({"messages": "Opps!.. ..Email already exists!"}), 400
            my_account = User(email, firstname, lastname, password)
            my_account = my_account.signup()
            my_account["user_id"] = len(user_list.get_all_users()) + 1
            user_list.add_user(my_account)
            return jsonify({"message": "You've sucessfully created an account"}), 201
        except Exception as e:
            e = {"Format": "Request format is invalid"}
            return jsonify(e), 400
    
    def user_signin(self):
        try:
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")
            user_details = [email, password]
            for detail in user_details:
                if detail.isspace() or len(detail) == 0:
                    return jsonify({"missing": "All fields must be filled"})
            if len(user_list.get_all_users()) == 0:
                return jsonify({"message": "Email does not exist"})
            for user in user_list.get_all_users():
                if user["email"] == email and user["password"] == password:
                    token = encode_auth_token(email).decode("utf-8")
                    return jsonify({"token": token, "message": "sucessfully logged in"})
                return jsonify({"message": "Oops... Invalid login credentials"})
        except Exception as e:
            e = {"Format": "Request format is invalid"}
            return jsonify(e), 400

