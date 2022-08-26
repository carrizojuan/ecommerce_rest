
from apps.products.api.serializers.general import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.base.api import GenericListApiView

class MeasureUnitListApiView(GenericListApiView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListApiView(GenericListApiView):
    serializer_class = CategoryProductSerializer


class IndicatorListApiView(GenericListApiView):
    serializer_class = IndicatorSerializer
