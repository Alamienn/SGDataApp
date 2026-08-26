import streamlit as st
import hashlib
import json
import os
from datetime import datetime, timedelta
import random
import string

USER_DB = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def init_user_db():
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w") as f:
            json.dump({}, f)

def load_users():
    init_user_db()
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=2)

def register_user(email, password, name, phone):
    users = load_users()
    if email in users:
        return False, "Email already registered"
    
    users[email] = {
        "name": name,
        "phone": phone,
        "password": hash_password(password),
        "balance": 0,
        "created": datetime.now().isoformat(),
        "verified": False,
        "verification_token": generate_token()
    }
    save_users(users)
    return True, "Registration successful. Please login."

def login_user(email, password):
    users = load_users()
    if email not in users:
        return False, "Email not found"
    if users[email]["password"] != hash_password(password):
        return False, "Incorrect password"
    return True, users[email]

def verify_email(token):
    users = load_users()
    for email, data in users.items():
        if data.get("verification_token") == token:
            data["verified"] = True
            data["verification_token"] = None
            save_users(users)
            return True, "Email verified successfully!"
    return False, "Invalid verification link"

def reset_password(email, new_password):
    users = load_users()
    if email not in users:
        return False, "User not found"
    users[email]["password"] = hash_password(new_password)
    save_users(users)
    return True, "Password reset successful"