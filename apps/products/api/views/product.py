from itertools import product
from os import stat
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status 

from apps.base.api import GenericListApiView
from apps.products.api.serializers.product import ProductSerializer

class ProductListApiView(GenericListApiView):
    serializer_class = ProductSerializer


class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)