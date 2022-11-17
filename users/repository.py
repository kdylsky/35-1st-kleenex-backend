from users.serializers import UserModelSerializer
from users.models import User
from users.utils.utils import author_provider 
from users.exceptions import NotFoundError

class UserRepo:
    def __init__(self)-> None:
        self.serializer = UserModelSerializer
        self.model = User

    def create(self, name, username, password, address, email, phone_number):
        data = {
            "name":name,
            "username":username,
            "password":password,
            "address":address,
            "email":email,
            "phone_number":phone_number
        }
        serializer = self.serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    
    def login(self, username, password):
        try:
            user_obj = self.model.objects.get(username=username)
            author_provider.check_request_password(password, user_obj.password)
            token = author_provider.create_token(user_obj.id)
            return token
        except User.DoesNotExist:
            raise NotFoundError()
