from products.models import Product, ProductImage, Taste, TasteByProduct, SubCategory, Category
from products.serializers import ProductModelSerializer, SubCategoryModelSerializer, TestProductModelSerializer,TestCategoryModelSerializer
from django.db.models import Q
class ProductRepo:
    def get(self, sort_field):
        product = Product.objects.all().order_by(f"-{sort_field}")[:3]
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
        total = Product.objects.all().count()
        products = Product.objects.filter(q).order_by(sort_dict.get(sorting)).distinct()[offset:offset+limit]
        serializer = ProductModelSerializer(products, many=True)
        return total, serializer.data