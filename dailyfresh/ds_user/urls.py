from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^register/$', views.register, name="register"),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^login/$', views.login, name="login"),
    url(r'^wishlist/$', views.wishlist, name="wishlist"),
    url(r'^register_exist/', views.login),
    url(r'^info/', views.info),
]