from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="SampleAPI",
      default_version='v1',
      description="Sample API Data To Use Accross Platforms",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

api_docs_urlpatterns = [
    path('api/v1/sampleAPI/', include("main_app.api_router")),
    # path('accounts/', include('rest_registration.api.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    # path('citizen/<str:uuid>/user/', SingleUserObjectView.as_view(), name="user"),
    path('api-auth-token/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
] + api_docs_urlpatterns
