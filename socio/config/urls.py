
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Backend API",
      default_version='v1',
      description="API endpoint docs for The Socio Platform",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes= ()
)

api_version = 'api/v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


   ## API Docs Endpoint 
   path(f'{api_version}/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(f'{api_version}/docs/re/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api-auth/', include('rest_framework.urls'))
]




'''
IN THIS SECTION , we are overwritng the Django default title, header and index title 
'''
### Admin panel Configure 
admin.site.site_header = "The Socio Platform"
admin.site.site_title = "Socio Backend"
admin.site.index_title = "Welcome to Socio"