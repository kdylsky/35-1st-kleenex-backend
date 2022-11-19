from users.utils.utils import author_provider
from users.repository import UserRepo


class UserService:
    def __init__(self)-> None:
        self.repo = UserRepo()
        
    def create(self, name: str, username: str, password: str, address: str, email: str, phone_number: str)-> dict:
        author_provider.check_username(username)
        author_provider.check_password(password)
        author_provider.check_phone_number(phone_number)
        author_provider.check_email(email)
        author_provider.duplicate_check_username(username)
        author_provider.duplicate_check_email(email)
        author_provider.duplicate_check_phone_number(phone_number)

        hashed_password  = author_provider.hash_password(password)
        created_user = self.repo.create(
            name         = name,
            username     = username,
            password     = hashed_password,
            address      = address,
            email        = email,
            phone_number = phone_number
        )
        return created_user

    def login(self, username: str, password: str)-> dict:
        token = self.repo.login(
            username = username,
            password = password
        )
        return token