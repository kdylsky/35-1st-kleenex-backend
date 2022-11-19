from rest_framework import status

from exceptions     import CustomBaseExecption

class SignupRaiseError(CustomBaseExecption):
    def __init__(self, msg):
        self.msg = msg
        self.status = status.HTTP_400_BAD_REQUEST


class CheckPasswordError(CustomBaseExecption):
    def __init__(self):
        self.msg = "Please Check your ID or Password"
        self.status = status.HTTP_400_BAD_REQUEST


class NotFoundError(CustomBaseExecption):
    def __init__(self):
        self.msg = "Not Found Object Error"
        self.status = status.HTTP_400_BAD_REQUEST
