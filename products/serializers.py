from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Image, Product


class ProductSerializer(serializers.ModelSerializer):
    # https://qiita.com/k_mawa82/items/1727c4355a94d5b51213
    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "product_text",
            "measurable_range",
            "option",
            "serial_number",
            "rank",
            "year_of_manufacture",
            "price",
            "description",
            "inventory_status",
            "brand",
            "category",
            "images",
        )

    def get_images(self, obj):  # pylint: disable=no-self-use
        try:
            return ImageSerializer(
                Image.objects.all().filter(product=Product.objects.get(id=obj.id)),
                many=True,
            ).data
        except:  # pylint: disable=bare-except
            return None


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "product",
            "image",
            "created_at",
            "updated_at",
        )
