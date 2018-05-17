from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^product/$', views.product, name="product"),
    url(r'^detail/$', views.detail, name="detail"),
]