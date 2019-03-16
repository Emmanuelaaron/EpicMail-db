import jwt
import datetime

def encode_auth_token(email):

    try:
        payload = {"exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1800),
                    "iat": datetime.datetime.utcnow(), "email": email}
        return jwt.encode(payload, "I Love what I am seeing")
    except Exception as e:
        return e