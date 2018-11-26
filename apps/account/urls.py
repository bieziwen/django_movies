from django.urls import path, re_path

from apps.account import views

urlpatterns=[
    path('hello/',views.test2),
    path('login/',views.login_view,name='login'),
    re_path(r'update/(\d+)',views.update),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('active/',views.user_active),
    path('inactive/',views.login_active,name='inactive')
]