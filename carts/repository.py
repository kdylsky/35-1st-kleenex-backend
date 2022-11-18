from carts.models import Cart
from products.models import Product
from carts.serializers import CartModelSerializer
from django.db import transaction
from carts.exceptions import NotFoundError

class CartRepo:
    def __init__(self):
        self.model = Cart
    
    def get(self, user: object)-> dict:
        cart_list = Cart.objects.select_related('product','user','size','graind')\
                                .prefetch_related('product__productimage_set')\
                                .filter(user=user)
        serializer = CartModelSerializer(cart_list, many=True)
        return serializer.data
    
    @transaction.atomic()
    def create(self, user: object, product_id: int, products: list)-> bool:
        try:
            target_product = Product.objects.get(id=product_id)
            for product in products:
                quantity = product["quantity"]
                graind   = target_product.graindbyproduct_set.get(grainding_id=product["graind"]).grainding
                size     = target_product.size_set.get(name=product["size"])
                cart, is_bool = self.model.objects.get_or_create(
                    user      = user,
                    product   = target_product,
                    graind    = graind,
                    size      = size,
                    defaults  = {'quantity':quantity}
                )
                if not is_bool :
                    cart.quantity += quantity
                    cart.save()
        except Product.DoesNotExist:
            raise NotFoundError()
        else:
            return True