from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include, re_path
from django.contrib import admin

schema_view = get_schema_view( 
    openapi.Info( 
        title="Swagger Study API", 
        default_version="v1", 
        description="Swagger Study를 위한 API 문서", 
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(name="test", email="test@test.com"), 
        license=openapi.License(name="Test License"), 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('user', include('users.urls')),
    path('products',include('products.urls')),
    path('cart',include('carts.urls')),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]


