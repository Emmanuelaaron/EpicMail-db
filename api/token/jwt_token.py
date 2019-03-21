import jwt
import datetime 

class authenticate:
    def encode_auth_token(self, email):

        try:
            payload = {"exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1800),
                        "iat": datetime.datetime.utcnow(), "email": email}
            return jwt.encode(payload, "I Love what I am seeing")   
        except Exception as e:
            return e

    def decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, "I Love what I am seeing")
            return payload['email']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
            