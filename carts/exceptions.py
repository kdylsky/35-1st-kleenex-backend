from rest_framework import status

from exceptions     import CustomBaseExecption


class NotFoundError(CustomBaseExecption):
    def __init__(self):
        self.msg = "Not Found Object Error"
        self.status = status.HTTP_400_BAD_REQUEST


class CanNotNegative(CustomBaseExecption):
    def __init__(self):
        self.msg = "Can Not Negative Number"
        self.status = status.HTTP_400_BAD_REQUEST
