from django.urls import path
from apps.users.api.api import user_api_view, user_detail_view

urlpatterns = [
    path('', user_api_view, name="usuarios_api"),
    path('<int:pk>', user_detail_view, name="usuario_detalle")
]
