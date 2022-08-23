from django.urls import path
from apps.users.api.api import UserApiView

urlpatterns = [
    path('', UserApiView.as_view(), name="usuarios_api")
]
