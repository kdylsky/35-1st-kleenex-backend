from django.db.models       import Q
from urllib.parse           import unquote

from products.models        import Product
from products.serializers   import ProductModelSerializer, ProductDetailSerializer
from products.exceptions    import NotFoundError


class ProductRepo:
    def __init__(self):
        self.model = Product

    def get(self, sort_field: str)-> dict:
        product     = self.model.objects.all().order_by(f"-{sort_field}")[:3]
        serializer  = ProductModelSerializer(product, many=True)
        return serializer.data
    
    def get_list(self, category: int, tastes: str, sorting: str, offset: int, limit: int)-> dict:
        q = Q()
        if category:
            q &= Q(subcategory_id = category)
        if tastes:
            q &= Q(taste__name__in = tastes)
        sort_dict = {
        'Highprice' : '-price',
        'Lowprice'  : 'price',
        'roast'     : '-roasting_date',
        None        : 'id'
        }
        total       = self.model.objects.all().count()
        products    = self.model.objects.filter(q).order_by(sort_dict.get(sorting)).distinct()[offset:offset+limit]
        serializer  = ProductModelSerializer(products, many=True)
        return total, serializer.data
    
    def get_detail(self, product_id: int)-> dict:
        try:
            product     = self.model.objects.get(id=product_id)
            serailizer  = ProductDetailSerializer(product)
            return serailizer.data
        except self.model.DoesNotExist:
            raise NotFoundError()
    
    def get_search(self, search: str)-> dict:
        products = Product.objects.filter(name__icontains=unquote(search))
        serializer = ProductModelSerializer(products, many=True)
        return serializer.data