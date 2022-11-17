from products.models import Product, ProductImage, Taste, TasteByProduct, SubCategory, Category
from products.serializers import ProductModelSerializer, SubCategoryModelSerializer, TestProductModelSerializer,TestCategoryModelSerializer

class ProductRepo:
    def get(self, sort_field):
        # p = Product.objects.get(id=1)
        # s = ProductModelSerializer(p, many=True)
        # print(s.data)
        
        # c = SubCategory.objects.get(id=1)
        # k = SubCategoryModelSerializer(c)
        # print(k.data)

        # s = TestProductModelSerializer(p)
        # print(s.data)

        t = SubCategory.objects.get(id=1)

        s = TestCategoryModelSerializer(t)
        print(s.data)
