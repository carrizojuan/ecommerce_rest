"""ecommerce_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.views import Login,  Logout, UserRefreshToken

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API ecommerce",
      default_version='v0.1',
      description="API REST",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="juancru68@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('refresh-token/', UserRefreshToken.as_view()),
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.routers'))
]
