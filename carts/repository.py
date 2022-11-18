from carts.models import Cart
from carts.serializers import CartModelSerializer

class CartRepo:
    def __init__(self):
        self.model = Cart
    
    def get(self, user: object)-> dict:
        cart_list = Cart.objects.select_related('product','user','size','graind')\
                                .prefetch_related('product__productimage_set')\
                                .filter(user=user)
        serializer = CartModelSerializer(cart_list,  many=True)
        return serializer.data