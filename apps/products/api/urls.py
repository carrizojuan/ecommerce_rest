from django.urls import path
from apps.products.api.views.general import MeasureUnitListApiView, CategoryProductListApiView, IndicatorListApiView

urlpatterns = [
    path('measure-units/', MeasureUnitListApiView.as_view(), name="measure_units"),
    path('category-products/', CategoryProductListApiView.as_view(), name="category_products"),
    path('indicators/', IndicatorListApiView.as_view(), name="indicators")
]