import streamlit as st
import json
import os
import subprocess

USER_DB = "users.json"
APP_TO_RUN = "MaTiGa5.4.3.py"  # Your uploaded file

# Load user data from file
def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

# Save user data to file
def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)

users = load_users()

st.title("🔐 MOHA Martigar App")

username = st.text_input("User Name")
password = st.text_input("Password", type="password")

col1, col2 = st.columns(2)

with col1:
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.balloons()
            st.info("🖥️ Launching desktop app...")

            # Run the GUI application after login
            try:
                subprocess.Popen(["python", APP_TO_RUN])
            except Exception as e:
                st.error(f"Error launching program: {e}")

        else:
            st.error("❌ Invalid username or password")

with col2:
    if st.button("Sign Up"):
        if not username or not password:
            st.warning("⚠️ Please enter both username and password")
        elif username in users:
            st.warning("⚠️ Username already exists")
        else:
            users[username] = password
            save_users(users)
            st.success("✅ Account created! Please log in.")

