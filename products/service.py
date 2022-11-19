from products.repository import ProductRepo

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepo()
    
    def get_product_mainpage(self)-> dict:
        """ 
        메인페이지의 파라미터
        가격, 신선도 정렬해서 상품 가지고 오기 
        """
        premiums        = self.product_repo.get("price")
        fresh_products  = self.product_repo.get("roasting_date")
        return {"가격":premiums, "신선도":fresh_products}
    
    def get_coffee_list(self, category: int, tastes: str, sorting: str, offset: int, limit: int)-> dict:
        """
        전체 상품리스트 출력
        - 필터링 있을시 필터링에 대한 데이터 출력
        """
        total, product = self.product_repo.get_list(category, tastes, sorting, offset, limit)
        data ={
            'total'             : total,
            'shop_product_list' : product
            }
        return data 
    
    def get_detail(self, product_id: int)-> dict:
        """
        특정 상품에 대한 데이터 출력
        """
        data = self.product_repo.get_detail(product_id=product_id) 
        return data
    
    def get_search(self, search: str)-> dict:
        """
        검색을 행한 데이터 출력
        """
        data = self.product_repo.get_search(search)
        return data