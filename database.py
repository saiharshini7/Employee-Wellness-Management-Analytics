import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


# -------------------------------
# Database Connection
# -------------------------------
def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conn

    except Exception as e:
        print("Database Connection Error:", e)
        return None


# -------------------------------
# Create Users Table
# -------------------------------
def create_users_table():
    conn = get_connection()

    if conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)

        conn.commit()
        cur.close()
        conn.close()


# -------------------------------
# Add New User
# -------------------------------
def add_user(name, email, password):
    conn = get_connection()

    if conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO users(name, email, password)
        VALUES(%s, %s, %s)
        """, (name, email, password))

        conn.commit()
        cur.close()
        conn.close()


# -------------------------------
# Get User by Email
# -------------------------------
def get_user(email):
    conn = get_connection()

    if conn:
        cur = conn.cursor()

        cur.execute("""
        SELECT * FROM users
        WHERE email=%s
        """, (email,))

        user = cur.fetchone()

        cur.close()
        conn.close()

        return user

    return None


# -------------------------------
# Update Password
# -------------------------------
def update_password(email, new_password):
    conn = get_connection()

    if conn:
        cur = conn.cursor()

        cur.execute("""
        UPDATE users
        SET password=%s
        WHERE email=%s
        """, (new_password, email))

        conn.commit()
        cur.close()
        conn.close()
def update_password(email, new_password):
    conn = get_connection()

    if conn:
        cur = conn.cursor()

        cur.execute("""
        UPDATE users
        SET password=%s
        WHERE email=%s
        """, (new_password, email))

        conn.commit()
        cur.close()
        conn.close()        