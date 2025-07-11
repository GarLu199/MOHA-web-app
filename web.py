import streamlit as st
import json
import os

# ------------ SETTINGS ------------
USER_DB = "users.json"

# ------------ DATABASE ------------
def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f)

users = load_users()

# ------------ LOGIN UI ------------
def login_form():
    st.title("🔐 Ministry Login")
    username = st.text_input("User Name")
    password = st.text_input("Password", type="password")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("✅ Logged in successfully!")
            else:
                st.error("❌ Invalid credentials")

    with col2:
        if st.button("Sign Up"):
            if not username or not password:
                st.warning("⚠️ Please enter both username and password")
            elif username in users:
                st.warning("⚠️ Username already exists")
            else:
                users[username] = password
                save_users(users)
                st.success("✅ Account created. Please log in.")

# ------------ POST-LOGIN UI ------------
def dashboard():
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Flag_of_Myanmar.svg/640px-Flag_of_Myanmar.svg.png", width=100)
    st.title("ပြည်ထဲရေးဝန်ကြီးဌာန")
    st.markdown("### ဗဟုသုတနှင့် သတင်းများ")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://via.placeholder.com/200x120?text=HOME+AFFAIRS", use_column_width=True)
        st.markdown("**အကြမ်းဖက်အဖွဲ့အစည်းများ စစ်တပ်အားတိုက်ခိုက်**")
        st.caption("10-07-2025")

    with col2:
        st.image("https://via.placeholder.com/200x120?text=MAP", use_column_width=True)
        st.markdown("**ကချင်ပြည်နယ်၌ တိုက်ပွဲဖြစ်ပွားမှု**")
        st.caption("10-07-2025")

    with col3:
        st.image("https://via.placeholder.com/200x120?text=TNLA", use_column_width=True)
        st.markdown("**TNLA တပ်ဖွဲ့နှင့် ပဋိပက္ခ**")
        st.caption("10-07-2025")

    st.markdown("---")
    st.markdown("📢 [သတင်းများအားလုံးကြည့်ရန်](#)")

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ------------ MAIN APP ------------
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        dashboard()
    else:
        login_form()

main()
