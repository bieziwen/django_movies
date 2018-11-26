from django.urls import path, re_path

from home import views

urlpatterns=[
    path('hello/',views.test1),
    path('update/',views.update),
    path('index/',views.index,name='index'),
    re_path(r'detail/(\d+)',views.detail,name='detail'),
    # re_path(r'detail1/(\d+)',views.detial1,name='detail1'),
    path('cate/',views.cate_movie,name='cate'),
]