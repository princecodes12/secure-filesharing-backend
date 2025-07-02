import jwt
from functools import wraps
from flask import jsonify, current_app, request
from app.models.user import User

def token_required(only_ops=False, only_client=False):
    def decorater(f):
        @wraps(f)
        def decorater_function(*args,**kwargs):
            token = None

            if 'Authorization' in request.headers:
                auth_header = request.headers['Authorization']
                if auth_header.startswith('Bearer '):
                    token = auth_header.split(" ")[1]
            
            if not token:
                return jsonify({'message' : 'Token is missing!'}),401
            
            try:
                payload = jwt.decode(token, current_app.config['JWT_SECERT_KEY'], algorithms=["HS256"])
                user = User.query.get(payload['user_id'])

                if not user:
                    return jsonify({"message": "Invalid user"}),401

                if only_ops and not user.is_ops_user:
                    return jsonify({"message": "Only ops users can access this route"}), 403

                if only_client and user.is_ops_user:
                    return jsonify({"message": "Only client users can access this route"}), 403

            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            
            return f(user,*args,**kwargs)
        return decorater_function
    return decorater
