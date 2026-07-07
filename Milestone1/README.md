# Employee Wellness Management Analytics

## Milestone 1 - User Authentication Module

### Project Objective

The objective of this project is to develop a secure User Authentication System for the Employee Wellness Management Analytics application using Streamlit and Neon PostgreSQL. The application provides user registration, login, forgot password, OTP verification, password reset, and a dashboard for authenticated users.

---

## Technologies Used

- Python
- Streamlit
- Neon PostgreSQL
- psycopg2
- bcrypt
- JWT (JSON Web Token)
- Google SMTP
- python-dotenv
- Pandas

---

## Features

### Home Page
- Welcome page
- Navigation to all modules

### User Registration
- Name
- Email
- Password
- Confirm Password
- Password hashing using bcrypt
- Data stored in Neon PostgreSQL

### Login
- Email and Password authentication
- JWT Token generation
- Session management

### Forgot Password
- Email verification
- OTP generation
- OTP sent through Google SMTP
- Password reset
- Password updated in PostgreSQL

### Dashboard
- Welcome message
- CSV File Upload

---

## Database

Database Used:

Neon PostgreSQL

Table:

users

Columns:

- id
- name
- email
- password

---

## Google Colab / VS Code Setup

1. Clone the repository

```bash
git clone <repository_link>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure the `.env` file with your Neon PostgreSQL and Gmail credentials.

4. Run the application

```bash
streamlit run app.py
```

---


---

## Outcome

Successfully implemented a secure authentication system with:

- User Registration
- Secure Login
- Password Encryption
- JWT Authentication
- Forgot Password
- OTP Verification
- Password Reset
- Dashboard
- CSV Upload
- Neon PostgreSQL Integration
