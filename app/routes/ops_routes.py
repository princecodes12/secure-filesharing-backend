from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User
from app.utils.token_helper import gen_token

ops_bp = Blueprint("ops",__name__)

@ops_bp.route("/signup",methods=["POST"])
def ops_signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 409
    
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(email=email,password=hashed_password,is_ops_user=True)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message":"User register successfully"}),201

@ops_bp.route("/login",methods = ["POST"])
def ops_login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message" : "Email and Password both required"}), 400
    
    user = User.query.filter_by(email=email,is_ops_user=True).first()

    if not user:
        return jsonify({"message" : "User not found"}),404

    if not bcrypt.check_password_hash(user.password,password):
        return jsonify({"message" : "Invalid Password"}),401
    
    token = gen_token(user.id,user.is_ops_user)

    return jsonify({"message" : "Login Successfull", "token" : token}),200 