from rest_framework import viewsets
from products_app.models import Product
from products_app.api.serializers import ProductSerializer

class ProductCRUDCBV(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer