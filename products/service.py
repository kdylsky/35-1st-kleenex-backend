from products.repository import ProductRepo

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepo()
    
    def get_product_mainpage(self):
        premiums        = self.product_repo.get("price")
        fresh_products  = self.product_repo.get("roasting_date")
        return {"가격":premiums, "신선도":fresh_products}
    
    def get_coffee_list(self, category, tastes,sorting, offset, limit):
        total,product = self.product_repo.get_list(category, tastes,sorting, offset, limit)
        result ={
            'total'             : total,
            'shop_product_list' : product
            }
        return result 