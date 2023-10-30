'''
Authentication
Filename: authentication.py

Author: Jacqueline
Created: 23/8/2023
Description: All functions related to authentication. Allows users to log in,
log out and ensures persistance of their data.

'''
import hashlib
import jwt
from database import database
from error import AccessError, InputError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import other as other

MINIMUM_PASSWORD_LENGTH = 6
MAX_FIRST_NAME_LENGTH = 50
MAX_LAST_NAME_LENGTH = 50
SENDER_ADDRESS = "wagwanians@gmail.com"
APP_PASS = "ppztlcftygxueizl"

def auth_login(email: str, password: str)->dict:
    store = database.get()
    users = store['users']

    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    for user_id, user in users.items():
        if email == user['email']:
            if hashed_input == user['password']:
                jwt = other.create_JWT(user_id)
                return {'token': jwt, 'auth_user_id': user_id, 'first_name': user['name_first']} # Success login
            else:
                raise InputError(description="Incorrect Password")
    raise InputError(description="Invalid Email")


def auth_register(email: str, password: str, name_first: str, name_last: str)->dict:
    if not other.is_valid_email(email):
        raise InputError(description="Email is not valid")
    if len(password) < MINIMUM_PASSWORD_LENGTH:
        raise InputError(description="Password is too short")
    if other.is_email_taken(email):
        raise InputError(description="Email is already taken")
    if len(name_first) < 1 or len(name_first) > MAX_FIRST_NAME_LENGTH:
        raise InputError(description="First name is too short or long")
    if len(name_last) < 1 or len(name_last) > MAX_LAST_NAME_LENGTH:
        raise InputError(description="Last name is too short or long")

    store = database.get()
    users = store['users']
    new_user_id = len(users)

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    new_user_dictionary = {'name_first': name_first, 'name_last': name_last, 'email': email,
                           'password': hashed_password, 'courses': [], 'sessions': []}
    users[new_user_id] = new_user_dictionary
    database.set(store)
    jwt = other.create_JWT(new_user_id)
    return {'token': jwt, 'auth_user_id': new_user_id}


def auth_logout(token):
    if not other.is_valid_JWT(token):
        raise AccessError(description="The token provided is not valid.")

    store = database.get()
    jwt_payload = jwt.decode(token, other.JWT_SECRET, algorithms=['HS256'])

    user = store['users'][jwt_payload['auth_user_id']]
    user['sessions'].remove(jwt_payload['user_session_id'])
    return {}


def password_reset_request(email):
    user_id = other.id_from_email(email)
    if user_id == None:
        return {}

    store = database.get()
    users = store['users']
    reset_codes = store['reset_codes']

    users[user_id]['sessions'] = []

    reset_code = str(other.generate_reset_code(email))
    reset_codes[reset_code] = user_id
    content = f"Your reset code is: {reset_code}"
    
    recovery_email = MIMEMultipart()
    recovery_email['Subject'] = "Password Reset Email" # message subject
    recovery_email['From'] = SENDER_ADDRESS
    recovery_email['To'] = email
    recovery_email.attach(MIMEText(content))  # message body

    # Login and send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login error
        try:
            server.login(SENDER_ADDRESS, APP_PASS)
        except smtplib.SMTPAuthenticationError:
            raise InputError("An error has occurred while trying to connect to SMTP server.")
        server.sendmail(SENDER_ADDRESS, email, recovery_email.as_string())
    return {}


def reset_user_password(reset_code: str, new_password: str):
    if len(new_password) < MINIMUM_PASSWORD_LENGTH:
        raise InputError("Proposed password is too short.")
    store = database.get()
    users = store['users']
    reset_codes = store['reset_codes']

    if reset_code not in reset_codes.keys():
        raise InputError("Reset code not valid.")

    user_id = reset_codes[reset_code]
    user = users[user_id]
    user['password'] = hashlib.sha256(new_password.encode()).hexdigest()

    database.set(store)
    return {}
