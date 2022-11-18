from carts.repository import CartRepo
from carts.exceptions import CanNotNegative
from carts.serializers import CartModelSerializer

class CartService:
    def __init__(self):
        self.repo = CartRepo()
    
    def get_list(self, user: object)-> dict:
        cart_list = self.repo.get(user)
        serializer = CartModelSerializer(cart_list, many=True)
        return serializer.data

    def create_cart(self, user: object, product_id: int, products: list)-> bool:
        self.repo.create(
            user=user,
            product_id=product_id,
            products=products
        )
        return True
    
    def patch_cart(self, user: object, cart_id: int, quantity: int)-> bool:
        cart_obj = self.repo.find(
            user=user,
            cart_id=cart_id
        )
        if quantity <= 0:
            raise CanNotNegative()
        cart_obj.quantity = quantity
        cart_obj.save()
        return True
        