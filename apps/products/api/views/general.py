
from apps.products.api.serializers.general import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.base.api import GenericListApiView
from rest_framework import viewsets

""" Api Views para listar, se hereda de GenericListApiView que utiliza generics.ListAPIView"""

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    queryset = serializer_class.Meta.model.objects.all()


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = serializer_class.Meta.model.objects.all()


class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    queryset = serializer_class.Meta.model.objects.all()
