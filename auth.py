import bcrypt
import jwt
import datetime

# Change this to a strong secret key in production
SECRET_KEY = "employee_wellness_secret_key"


# -------------------------------
# Hash Password
# -------------------------------
def hash_password(password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hashed.decode()


# -------------------------------
# Verify Password
# -------------------------------
def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )


# -------------------------------
# Generate JWT Token
# -------------------------------
def generate_token(email):

    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token


# -------------------------------
# Verify JWT Token
# -------------------------------
def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None