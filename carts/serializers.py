from rest_framework  import serializers

from carts.models    import Cart
from products.models import ProductImage


class ProductImageModelSerializer(serializers.ModelSerializer):
    """
    Cart리스트에서 상품이미지 참조를 위한 serializer
    """
    class Meta:
        model  = ProductImage
        fields = "url",


class CartModelSerializer(serializers.ModelSerializer):
    """
    Cart 리스트 출력을 위한 serializer
    """
    product_id = serializers.PrimaryKeyRelatedField(source="product.id",read_only=True)
    user       = serializers.PrimaryKeyRelatedField(source="user.name",read_only=True)
    product    = serializers.PrimaryKeyRelatedField(source="product.name",read_only=True)
    size       = serializers.PrimaryKeyRelatedField(source="size.name",read_only=True)
    graind     = serializers.PrimaryKeyRelatedField(source="graind.type",read_only=True)
    price      = serializers.PrimaryKeyRelatedField(source="size.price", read_only=True)
    image      = ProductImageModelSerializer(source="product.productimage_set", many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "id", "product_id", "user", "product","size", "graind", "quantity", "price", "image"


class CartDeatilRequestSchema(serializers.Serializer):
    """
    CartRequsetSchema 리스트 파라미터를 위한 중첩 serializer
    """
    size     = serializers.CharField(max_length=10)
    graind   = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartRequetSchema(serializers.Serializer):
    """
    Cart객체 생성을 위한 요청 파라미터 serializer 정의
    """
    product_id  = serializers.IntegerField()
    products    = CartDeatilRequestSchema(many=True)


class CartPatchSchema(serializers.Serializer):
    """
    Cart객체 수정을 위한 요청 파라미터 serializer 정의
    """
    cart_id  = serializers.IntegerField()
    quantity = serializers.IntegerField()