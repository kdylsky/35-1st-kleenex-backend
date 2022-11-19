import re
import jwt
import bcrypt
from datetime import datetime

from django.conf import settings

from users.models       import User
from users.exceptions   import SignupRaiseError, CheckPasswordError

class AuthorProvider:
    def __init__(self):
        self.key = settings.JWT_KEY
        self.expire_sec = settings.JWT_EXPIRE_TIME
        self.refresh_expire_sec = settings.JWT_REFRESH_EXPIRE_TIME
    
    def check_username(self, username: str)-> bool:
        REGEX_USERNAME = "^[A-Za-z0-9]{4,12}$"
        if not re.match(REGEX_USERNAME, username):
            raise SignupRaiseError("INVALID_USERNAME_FORMAT")

    def check_password(self, password: str)-> bool:
        REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
        if not re.match(REGEX_PASSWORD, password):
            raise SignupRaiseError("INVALID_PASSWORD_FORMAT")

    def check_email(self, email: str)-> bool:
        REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(REGEX_EMAIL, email):
            raise SignupRaiseError("INVALID_EMAIL_FORMAT")

    def check_phone_number(self, phone_number: str)-> bool:
        REGEX_PHONE_NUMBER = '^\d{3}-\d{3,4}-\d{4}$'
        if not re.match(REGEX_PHONE_NUMBER, phone_number):
            raise SignupRaiseError("INVALID_PHONE_NUMBER_FORMAT")

    def duplicate_check_username(self, username: str)-> bool:
        if User.objects.filter(username = username).exists():
            raise SignupRaiseError("INVILD_USERNAME")

    def duplicate_check_email(self, email: str)-> bool:
        if User.objects.filter(email = email).exists():
            raise SignupRaiseError("INVAILD_EMAIL")

    def duplicate_check_phone_number(self, phone_number: str)-> bool:
        if User.objects.filter(phone_number = phone_number).exists():
            raise SignupRaiseError("INVAILD_PHONE_NUMBER")

    def hash_password(self, password: str)-> bool:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_request_password(self, password: str, user_password: str)-> bool:
        flag = bcrypt.checkpw(password.encode("utf-8"), user_password.encode("utf-8"))
        if not flag:
            raise CheckPasswordError
        return flag

    def create_token(self, user_id: int, is_expired = False)-> dict:
        exp = 0 if is_expired else self.get_curr_sec() + self.expire_sec
        token = jwt.encode({"user_id":user_id, "exp":exp}, self.key, algorithm="HS256")
        return {"access": token}

    def get_curr_sec(self)-> str:
        return datetime.now().timestamp()
    

author_provider= AuthorProvider()