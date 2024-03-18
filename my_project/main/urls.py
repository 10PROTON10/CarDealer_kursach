"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from api import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
# from api.views import *
# from rest_framework import routers
#
# router = routers.SimpleRouter()
# router.register(r'brand', BrandListView)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('api/', include('api.urls')),
    path('', include('homepage.urls')),
]

# В режиме разработки добавляем обработку статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # path('api/v1/', include(router.urls.py)),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # # path('api/v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/', custom_login_view, name='custom_login'),

