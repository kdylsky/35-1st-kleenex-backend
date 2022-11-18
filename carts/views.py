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


cart_service = CartService()

class CartAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return get_cart_list(request, *args, **kwargs)

@execption_hanlder()
@parser_classes([JSONParser])
@login_decorators()
def get_cart_list(request, *args, **kwargs):
    user = request.user
    return JsonResponse(cart_service.get_list(user), status=status.HTTP_200_OK, safe=False)



class CartView(View):
    @login_decorator
    @transaction.atomic()
    def post(self, request):
        try:
            datas           = json.loads(request.body)
            user            = request.user
            product_id      = datas["product_id"]
            products        = datas["product"]
            target_product  = Product.objects.get(id = product_id)
            
            for product in products:
                quantity    = product["quantity"]
                graind      = target_product.graindbyproduct_set.get(grainding_id = product["graind"]).grainding
                size        = target_product.size_set.get(name = product["size"])

                cart, is_bool   = Cart.objects.get_or_create(
                    user        = user,
                    product     = target_product,
                    graind      = graind,
                    size        = size,
                    defaults    = {'quantity': quantity}
                )

                if not is_bool :
                    cart.quantity += quantity
                    cart.save()

            return JsonResponse({"MESSAGE": "TEST"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEYERROR"}, status=400)

        except Size.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_SIZE"}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_PRODUCT"}, status=400)

        except Grainding.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_GRAINDING"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse

        except GraindByProduct.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_GRAINDING"}, status=400)

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