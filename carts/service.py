from carts.repository import CartRepo


class CartService:
    def __init__(self):
        self.repo = CartRepo()
    
    def get_list(self, user: object)-> dict:
        data = self.repo.get(user)
        return data