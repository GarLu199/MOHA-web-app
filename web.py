import streamlit as st

# Temporary in-memory user store (can be replaced with a database)
users = {"admin": "1234"}

st.title("🔐 Simple Login App")

# Input fields
username = st.text_input("User Name")
password = st.text_input("Password", type="password")

# Two buttons side-by-side
col1, col2 = st.columns(2)

# Login button
with col1:
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.balloons()
        else:
            st.error("❌ Invalid username or password")

# Sign Up button
with col2:
    if st.button("Sign Up"):
        if username == "" or password == "":
            st.warning("⚠️ Please enter a username and password")
        elif username in users:
            st.warning("⚠️ Username already exists")
        else:
            users[username] = password
            st.success("✅ Account created! You can now login.")
