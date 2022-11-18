from django.db          import transaction

from carts.models       import Cart
from carts.exceptions   import NotFoundError
from products.models    import Product

class CartRepo:
    def __init__(self):
        self.model = Cart
    
    def get(self, user: object)-> object:
        cart_list = self.model.objects.select_related('product','user','size','graind')\
                                .prefetch_related('product__productimage_set')\
                                .filter(user=user)
        return cart_list
    
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
    
    def find(self, user: object, cart_id: int)-> object:
        try:
            cart_obj = self.model.objects.get(id=cart_id, user=user) 
        except self.model.DoesNotExist:
            raise NotFoundError()
        else:
            return cart_obj