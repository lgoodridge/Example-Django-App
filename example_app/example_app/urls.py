"""
Example app URL configuration.
"""

from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', include('core.urls')),
]
