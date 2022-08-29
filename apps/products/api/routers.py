from rest_framework import routers
from apps.products.api.views.product import ProductViewSet
from apps.products.api.views.general import MeasureUnitViewSet, IndicatorViewSet, CategoryProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'measure-units', MeasureUnitViewSet, basename='measure_units')
router.register(r'indicators', IndicatorViewSet, basename='indicators')
router.register(r'categories', CategoryProductViewSet, basename='categories')

urlpatterns = router.urls