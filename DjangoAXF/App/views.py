from django.shortcuts import render

# Create your views here.
from App.models import WheelModel, NavModel


def home(request):
    wheels = WheelModel.objects.all()
    navs = NavModel.objects.all()

    data = {
        "title":"首页",
        "wheels":wheels,
        "navs":navs
    }
    return render(request, 'home/home.html', context=data)
def market(request):
    data = {
        "title": "闪购超市",
    }
    return render(request, 'market/market.html', context=data)
def cart(request):
    data = {
        "title": "购物车",
    }
    return render(request, 'cart/cart.html', context=data)
def mine(request):
    data = {
        "title": "我的",
    }
    return render(request, 'mine/mine.html', context=data)