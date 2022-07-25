import json

from django.http import JsonResponse
from django.views import View

from carts.models import Cart
from products.models import *
from core.utils import login_decorator

class CartView(View):
    @login_decorator
    def patch(self,request):
        try:
            data            = json.loads(request.body)
            cart            = Cart.objects.get(id=data["cart_id"])
            quantity        = data["quantity"]
            cart.quantity   = quantity
            cart.save()

            if cart.quantity <= 0:
                cart.quantity = 1
                cart.save()

            return JsonResponse({"MESSAGE": "PATCH_SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

        except Cart.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_CART"}, status=400)

        except Size.DoesNotExist:
            return JsonResponse({"MESSAGE": "DOESNOTEXIST_SIZE"}, status=400)