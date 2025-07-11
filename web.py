import streamlit as st

# Page title
st.title("🔐 MOHA Login App")

# Input fields
username = st.text_input("User Name")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("✅ Login Successful")
        st.balloons()
    else:
        st.error("❌ Invalid username or password")
