from django.urls import path
from apps.products.api.views.general import MeasureUnitListApiView, CategoryProductListApiView, IndicatorListApiView
from apps.products.api.views.product import ProductListCreateApiView, ProductDetailApiView, ProductDeleteApiView, ProductUpdateApiView

urlpatterns = [
    path('measure-units/', MeasureUnitListApiView.as_view(), name="measure_units"),
    path('category-products/', CategoryProductListApiView.as_view(), name="category_products"),
    path('indicators/', IndicatorListApiView.as_view(), name="indicators"),
    path('product/', ProductListCreateApiView.as_view(), name="product_create"),
    path('product/detail/<int:pk>', ProductDetailApiView.as_view(), name="product_detail"),
    path('product/delete/<int:pk>', ProductDeleteApiView.as_view(), name="product_delete"),
    path('product/update/<int:pk>', ProductUpdateApiView.as_view(), name="product_update"),
]