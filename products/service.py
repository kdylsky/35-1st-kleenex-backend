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
        data ={
            'total'             : total,
            'shop_product_list' : product
            }
        return data 
    
    def get_detail(self, product_id):
        data = self.product_repo.get_detail(product_id = product_id) 
        return data
    
    def get_search(self, search):
        data = self.product_repo.get_search(search)
        return data