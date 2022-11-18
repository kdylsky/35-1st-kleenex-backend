from rest_framework import serializers
from products.models import Product, ProductImage, Taste, TasteByProduct, Category, SubCategory

## 중첩 serializer 1:N관계에서 1에 해당하는 시리얼 라이즈


class TasteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = "id", "name"

class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "id","url" 

class ProductModelSerializer(serializers.ModelSerializer):
    productimage_set= ProductImageModelSerializer(many=True, read_only=True)
    taste_set =  TasteModelSerializer(many=True, read_only = True)
    class Meta:
        model = Product
        fields = "id","name", "eng_name", "roasting_date", "price",  "productimage_set", "taste_set"





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