from rest_framework  import serializers

from products.models import Product, ProductImage, Taste, Category, SubCategory, Size, Grainding

class TasteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = "id", "name"


class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "id","url" 


class ProductModelSerializer(serializers.ModelSerializer):
    """
    상품에 대한 serializer
    상품이미지와 맛에 대한 중첩 serializer를 포함한다.
    """
    productimage_set = ProductImageModelSerializer(many=True, read_only=True)
    taste_set        =  TasteModelSerializer(many=True, read_only = True)
    class Meta:
        model   = Product
        fields  = "id","name", "eng_name", "roasting_date", "price",  "productimage_set", "taste_set"


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "id","name","price"


class GraindingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grainding
        fields = "id", "type"


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품에 대한 serializer
    상품이미지, 맛, 사이즈, 상품의 갈린정도에 대한 중첩 serializer를 포함한다.
    """
    productimage_set= ProductImageModelSerializer(many=True, read_only=True)
    taste_set =  TasteModelSerializer(many=True, read_only = True)
    size_set = SizeModelSerializer(many=True, read_only = True)
    grainding_set = GraindingModelSerializer(many=True, read_only = True)
    
    class Meta:
        model = Product
        fields = "id","name", "eng_name", "roasting_date", "price",  "productimage_set", "taste_set", "grainding_set", "size_set"












class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategoryModelSerializer(instance.category).data
        return response


class TestProductModelSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="productimage_set.id")
    class Meta:
        model = Product
        fields = "url", "name"


# 1:N의 경우에서 n에 해당하는 값이 1에 접근하고자 하는 경우 source를 사용해서 필드까지 접근이 가능하다.
class TestCategoryModelSerializer(serializers.ModelSerializer):
    test = serializers.CharField(source="category.name")
    class Meta:
        model = SubCategory
        fields = "__all__"