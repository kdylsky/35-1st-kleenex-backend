from rest_framework import status

from exceptions     import CustomBaseExecption


class NotFoundError(CustomBaseExecption):
    def __init__(self):
        self.msg = "Not Found Object Error"
        self.status = status.HTTP_400_BAD_REQUEST
