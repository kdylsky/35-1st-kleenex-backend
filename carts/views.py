from django.http                import JsonResponse

from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.parsers     import JSONParser
from rest_framework.decorators  import parser_classes

from carts.service                import CartService
from carts.serializers            import CartRequetSchema, CartPatchSchema
from decorators.auth_handler      import login_decorators
from decorators.execption_handler import execption_hanlder

cart_service = CartService()

class CartAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return get_cart_list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return create_cart(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return patch_cart(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return delete_cart(request, *args, **kwargs)

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
    user   = request.user
    data   = request.data
    params = CartRequetSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(cart_service.create_cart(user, **params.data), status=status.HTTP_201_CREATED, safe=False)

@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def patch_cart(request, *args, **kwargs):
    user   = request.user
    data   = request.data
    params = CartPatchSchema(data=data)
    params.is_valid(raise_exception=True)
    return JsonResponse(cart_service.patch_cart(user, **params.data), status=status.HTTP_201_CREATED, safe=False)
    
@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def delete_cart(request, *args, **kwargs):
    user    = request.user
    cart_id = kwargs["cart_id"]
    return JsonResponse(cart_service.delete_cart(user, cart_id), status=status.HTTP_200_OK, safe=False)