from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    this is serializer which is just like a normal serializer is just
    that it contains some set of populated fields
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "inventory_quantity",
        ]
        # fields that are not need when making post request
        read_only_fields = ["id"]
