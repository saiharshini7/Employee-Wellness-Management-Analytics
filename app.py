from auth import generate_token
import streamlit as st
import bcrypt
from database import create_users_table, add_user, get_user

# Create table if it doesn't exist
create_users_table()

st.set_page_config(
    page_title="Employee Wellness Management Analytics",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Employee Wellness Management Analytics")

# Sidebar Navigation

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Sign Up", "Login", "Forgot Password", "Dashboard"]
)

# ---------------- HOME ----------------
if page == "Home":
    st.header("🏠 Home")
    st.write("Welcome to Employee Wellness Management Analytics")
    st.write("Please Sign Up or Login from the sidebar.")

# ---------------- SIGN UP ----------------
elif page == "Sign Up":

    st.header("👤 Sign Up")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):

        if name == "" or email == "" or password == "":
            st.error("All fields are required")

        elif password != confirm:
            st.error("Passwords do not match")

        elif get_user(email):
            st.error("Email already registered")

        else:
            hashed = bcrypt.hashpw(
                password.encode(),
                bcrypt.gensalt()
            ).decode()

            add_user(name, email, hashed)

            st.success("Registration Successful!")

# ---------------- LOGIN ----------------
elif page == "Login":

    st.header("🔑 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = get_user(email)

        if user:

            stored_password = user[3]

            if bcrypt.checkpw(
                password.encode(),
                stored_password.encode()
            ):

                token = generate_token(email)

                st.session_state["logged_in"] = True
                st.session_state["token"] = token
                st.session_state["username"] = user[1]

                st.success("Login Successful!")

            else:
                st.error("Incorrect Password")

        else:
            st.error("User Not Found")
elif page == "Forgot Password":

    st.header("🔒 Forgot Password")

    email = st.text_input("Registered Email")

    if "otp" not in st.session_state:
        st.session_state.otp = ""

    if st.button("Generate OTP"):

        user = get_user(email)

        if user:

            otp = generate_otp()

            st.session_state.otp = otp
            st.session_state.reset_email = email

            if send_otp(email, otp):
                st.success("OTP Sent Successfully")
            else:
                st.error("Failed to Send OTP")

        else:
            st.error("Email Not Registered")

    entered_otp = st.text_input("Enter OTP")

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Reset Password"):

        if entered_otp != st.session_state.otp:
            st.error("Invalid OTP")

        elif new_password != confirm_password:
            st.error("Passwords Do Not Match")

        else:

            hashed = bcrypt.hashpw(
                new_password.encode(),
                bcrypt.gensalt()
            ).decode()

            update_password(
                st.session_state.reset_email,
                hashed
            )

            st.success("Password Updated Successfully")
# ---------------- DASHBOARD ----------------
elif page == "Dashboard":

    if st.session_state.get("logged_in"):

        st.header("📊 Dashboard")

        st.success(f"Welcome {st.session_state['username']}")

        if st.button("Logout"):
            st.session_state.clear()
            st.success("Logged Out Successfully")

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is not None:
            import pandas as pd

            df = pd.read_csv(uploaded_file)

            st.write(df)

            st.success("CSV Uploaded Successfully!")

    else:
        st.warning("Please Login First.")


from database import update_password
from email_utils import generate_otp, send_otp
import random        