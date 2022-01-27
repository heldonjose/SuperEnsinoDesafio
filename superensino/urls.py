from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sistemas de questões",
        default_version='v1',
        description="Api de dados para o sistemas de questões.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="heldonjose@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# url Swagger-----------------------------------------------
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
# urls includes API DRF---------------------------------------
urlpatterns += [
    path('api/academic/', include('apps.academic.api.urls')),
]

# BASIC url-----------------------------------------
urlpatterns += [
    path('', admin.site.urls),
]
