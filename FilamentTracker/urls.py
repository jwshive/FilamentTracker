"""
URL configuration for FilamentTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from tracker.views import get_configurations, filament_config_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_configurations, name='all_configs'),
    path('config/<int:id>', filament_config_detail, name='config_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
