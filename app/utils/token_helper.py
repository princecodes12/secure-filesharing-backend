import jwt
from datetime import datetime, timedelta
from flask import current_app

def gen_token(user_id,is_ops_user):
    payload = {
        'user_id' : user_id,
        'is_ops_user' : is_ops_user,
        'exp' : datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload,current_app.config['JWT_SECRET_KEY'],algorithm='HS256')
    return token