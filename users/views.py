from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from users.service import UserService
from users.serializers import UserModelSerializer, LoginSchema
from decorators.execption_handler import execption_hanlder
# content_type을 확인해서 request.data에 담아준다는 의미이다.?
# parser클래스를 정의함으로써 내가 원하느content_type이 아닌 경우에는 오류가 발생?
# 들어오는 요청의 헤더를 검사한다.

user_service = UserService()

@execption_hanlder()
@api_view(['POST'])
@parser_classes([JSONParser])
def signup(request, *args, **kwargs):
    data    = request.data
    params  = UserModelSerializer(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.create(**params.data), status=status.HTTP_201_CREATED)

@execption_hanlder()
@api_view(['POST'])
@parser_classes([JSONParser])
def login(request, *args, **kwargs):
    data = request.data
    params = LoginSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.login(**params.data), status=status.HTTP_200_OK)