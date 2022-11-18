from django.http import JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes, api_view
from drf_yasg.utils import swagger_auto_schema

from users.service import UserService
from users.serializers import UserModelSerializer, LoginSchema
from decorators.execption_handler import execption_hanlder

user_service = UserService()

@api_view(['POST'])
@execption_hanlder()
@parser_classes([JSONParser])
@swagger_auto_schema(
    request_body=UserModelSerializer,
    responses={201: UserModelSerializer},
)
def signup(request, *args, **kwargs):
    data    = request.data
    params  = UserModelSerializer(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.create(**params.data), status=status.HTTP_201_CREATED)


@api_view(['POST'])
@execption_hanlder()
@parser_classes([JSONParser])
@swagger_auto_schema(
    responses={"access": "encoded_jwt"},
)
def login(request, *args, **kwargs):
    data    = request.data
    params  = LoginSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(user_service.login(**params.data), status=status.HTTP_200_OK)