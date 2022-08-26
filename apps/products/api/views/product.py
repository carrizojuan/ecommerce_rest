from apps.base.api import GenericListApiView
from apps.products.api.serializers.product import ProductSerializer

class ProductListApiView(GenericListApiView):
    serializer_class = ProductSerializer