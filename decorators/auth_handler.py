import jwt
from functools import wraps
from users.models import User
from users.utils.utils import author_provider
from users.exceptions import NotFoundError 
from exceptions import NotAuthorizedError

def login_decorators():
    def decorator(api_func):
        @wraps(api_func)
        def wrapper(request, *args, **kwargs):
            try:
                access_token = request.headers.get('Authorization', None)     
                if access_token == None: 
                    raise NotAuthorizedError()                
                payload = jwt.decode(access_token, author_provider.key, algorithms=["HS256"])                
                user         = User.objects.get(id = payload['user_id'])
                request.user = user
                return api_func(request, *args, **kwargs)
            except User.DoesNotExist:
                raise NotFoundError()        
        return wrapper
    return decorator