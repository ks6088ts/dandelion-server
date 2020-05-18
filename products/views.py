from rest_framework import viewsets

from .models import Image, Product
from .serializers import ImageSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get"]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ["get"]
