from django.urls import path
from apps.products.api.views.general import MeasureUnitListApiView, CategoryProductListApiView, IndicatorListApiView
from apps.products.api.views.product import ProductListApiView, ProductCreateApiView

urlpatterns = [
    path('measure-units/', MeasureUnitListApiView.as_view(), name="measure_units"),
    path('category-products/', CategoryProductListApiView.as_view(), name="category_products"),
    path('indicators/', IndicatorListApiView.as_view(), name="indicators"),
    path('product/create', ProductCreateApiView.as_view(), name="product_create"),
    path('product/', ProductListApiView.as_view(), name="products"),
    
]