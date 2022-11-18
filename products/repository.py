from products.models import Product
from products.serializers import ProductModelSerializer, ProductDetailSerializer
from django.db.models import Q
from urllib.parse          import unquote

class ProductRepo:
    def __init__(self):
        self.model = Product

    def get(self, sort_field):
        product = self.model.objects.all().order_by(f"-{sort_field}")[:3]
        serializer = ProductModelSerializer(product, many=True)
        return serializer.data
    
    def get_list(self, category, tastes,sorting, offset, limit):
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
        total = self.model.objects.all().count()
        products = self.model.objects.filter(q).order_by(sort_dict.get(sorting)).distinct()[offset:offset+limit]
        serializer = ProductModelSerializer(products, many=True)
        return total, serializer.data
    
    def get_detail(self, product_id):
        product = self.model.objects.get(id=product_id)
        serailizer = ProductDetailSerializer(product)
        return serailizer.data

    def get_search(self, search):
        products = Product.objects.filter(name__icontains=unquote(search))
        serializer = ProductModelSerializer(products, many=True)
        return serializer.data