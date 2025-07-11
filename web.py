import streamlit as st
import json
import os

# Path to user database file
USER_DB = "users.json"

# Load user data from file
def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as file:
            return json.load(file)
    return {}

# Save user data to file
def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file)

# Load existing users
users = load_users()

st.title("🔐 Simple Login & Signup App")

# Input fields
username = st.text_input("User Name")
password = st.text_input("Password", type="password")

# Columns for buttons
col1, col2 = st.columns(2)

# Login
with col1:
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.balloons()
        else:
            st.error("❌ Invalid username or password")

# Sign Up
with col2:
    if st.button("Sign Up"):
        if username == "" or password == "":
            st.warning("⚠️ Please enter both username and password")
        elif username in users:
            st.warning("⚠️ Username already exists")
        else:
            users[username] = password
            save_users(users)
            st.success("✅ Account created! You can now login.")
