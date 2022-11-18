from carts.repository import CartRepo


class CartService:
    def __init__(self):
        self.repo = CartRepo()
    
    def get_list(self, user: object)-> dict:
        data = self.repo.get(user)
        return data
    
    def create_cart(self, user: object, product_id: int, products: list)-> bool:
        self.repo.create(
            user=user,
            product_id=product_id,
            products=products
        )
        return True