from products.repository import ProductRepo

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepo()
    
    def get_product_mainpage(self):
        price_product = self.product_repo.get("price")
        # premiums_product = self.product_repo.get("premiums")