from carts.models import Cart
from products.models import Product, Size, Grainding, ProductImage
from rest_framework import serializers


class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "url",


class CartModelSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source="product.id",read_only=True)
    user = serializers.PrimaryKeyRelatedField(source="user.name",read_only=True)
    product = serializers.PrimaryKeyRelatedField(source="product.name",read_only=True)
    size = serializers.PrimaryKeyRelatedField(source="size.name",read_only=True)
    graind = serializers.PrimaryKeyRelatedField(source="graind.type",read_only=True)
    price = serializers.PrimaryKeyRelatedField(source="size.price", read_only=True)
    image = ProductImageModelSerializer(source="product.productimage_set", many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "id", "product_id", "user", "product","size", "graind", "quantity", "price", "image"

class CartDeatilRequest(serializers.Serializer):
    size = serializers.CharField(max_length=10)
    graind = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartRequet(serializers.Serializer):
    product_id = serializers.IntegerField()
    products = CartDeatilRequest(many=True)


class CartPatchSchema(serializers.Serializer):
    cart_id = serializers.IntegerField()
    quantity = serializers.IntegerField()