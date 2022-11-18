import json

from django.db import transaction
from django.http import JsonResponse
from django.views import View

from carts.models import Cart
from products.models import *
from core.utils import login_decorator

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from decorators.auth_handler import login_decorators
from decorators.execption_handler import execption_hanlder
from django.http import JsonResponse

from carts.service import CartService
from carts.serializers import CartRequet, CartPatchSchema

cart_service = CartService()

class CartAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return get_cart_list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return create_cart(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return patch_cart(request, *args, **kwargs)

@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def get_cart_list(request, *args, **kwargs)-> dict:
    user = request.user
    return JsonResponse(cart_service.get_list(user), status=status.HTTP_200_OK, safe=False)

@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def create_cart(request, *args, **kwargs)-> bool:
    user = request.user
    data = request.data
    params = CartRequet(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(cart_service.create_cart(user, **params.data), status=status.HTTP_201_CREATED, safe=False)


@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def patch_cart(request, *args, **kwargs):
    user = request.user
    data = request.data
    params = CartPatchSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(cart_service.patch_cart(user, **params.data), status=status.HTTP_201_CREATED, safe=False)
    

class CartView(View):
    @login_decorator
    def patch(self,request):
        try:
            data            = json.loads(request.body)
            user            = request.user
            cart            = Cart.objects.get(id=data["cart_id"], user=user)
            quantity        = data["quantity"]

            if quantity <= 0:
                return JsonResponse({'MESSAGE' : f'INVALID VALUE : {quantity} '}, status=400)
            
            cart.quantity = quantity
            cart.save()

            return JsonResponse({"MESSAGE": "PATCH_SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

        except Cart.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_CART"}, status=400)

    @login_decorator
    def delete(self, request):
        try:
            datas = json.loads(request.body)
            user = request.user 
            if datas.get("is_bool"):
                Cart.objects.filter(user=user).delete()

            elif datas.get("cart_id"):
                for data in datas["cart_id"]:
                    Cart.objects.get(id=data, user=user).delete()

            return JsonResponse({"MESSAGE": "DELETE_SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

        except Cart.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_CART"}, status=400)