
from django.contrib import admin
from django.urls import path, include, re_path

from apps.home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('',views.index),
    path('home/', include('apps.home.urls')),
    path('account/', include('apps.account.urls')),
]
