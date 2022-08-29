from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, viewsets 

from apps.base.api import GenericListApiView
from apps.products.api.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def create(self, request):
        product_serializer = self.get_serializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Error no existe este producto"}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = self.get_serializer().Meta.model.objects.get(id=pk)
        if product:
            product.state = False
            product.save()
            return Response({"message": "Producto eliminado correctamente"}, status=status.HTTP_200_OK)
        return Response(self.get_serializer().errors, status=status.HTTP_400_BAD_REQUEST)


""" ListCreateAPIView es una vista generica para el listado y creacion de un modelo"""

""" class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state=True)

    #se sobreescribe el metodo post que tiene CreateAPIView para personalizarlo 

    def post(self, request):
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message': 'Producto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    
    def put(self, request, pk):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Error no existe este producto"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        product = self.get_serializer().Meta.model.objects.get(id=pk)
        if product:
            product.state = False
            product.save()
            return Response({"message": "Producto eliminado correctamente"}, status=status.HTTP_200_OK)
        return Response(self.get_serializer().errors, status=status.HTTP_400_BAD_REQUEST) """
