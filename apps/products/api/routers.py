from rest_framework import routers
from apps.products.api.views.product import ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls