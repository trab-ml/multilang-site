from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from main import views

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    prefix_default_language=False,
)
