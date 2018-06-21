from django.shortcuts import render

# Create your views here.
from App.models import WheelModel, NavModel, MustBuyModel, ShopModel, MainShow, FoodTypes, Goods


def home(request):
    wheels = WheelModel.objects.all()
    navs = NavModel.objects.all()
    mustbuys =MustBuyModel.objects.all()
    cvsList =ShopModel.objects.all()
    mainshows = MainShow.objects.all()

    shop_0 = cvsList[:1]
    shop_1 = cvsList[1:3]
    shop_2 = cvsList[3:7]
    shop_3 = cvsList[7:11]

    data = {
        "title":"首页",
        "wheels":wheels,
        "navs":navs,
        "mustbuys": mustbuys,
        "mainshows": mainshows,
        "shop_0": shop_0,
        "shop_1_3": shop_1,
        "shop_3_7": shop_2,
        "shop_7_11": shop_3,
    }
    return render(request, 'home/home.html', context=data)
def market(request):
    typeid = request.GET.get("typeid", 104749)
    childid = request.GET.get("childid", 0)
    orderby = int(request.GET.get("orderby", 0))
    foodtypes = FoodTypes.objects.all()

    fts = FoodTypes.objects.filter(typeid=typeid).first()
    child = fts.childtypenames

    if childid == 0:
        goods = Goods.objects.filter(categoryid=typeid)
    else:
        goods = Goods.objects.filter(categoryid=typeid, childcid=childid)

    #
    # if orderby == 1:
    #     goods.order_by("productnum")
    # elif orderby ==2:
    #     goods.order_by("price")
    # elif orderby ==3:
    #     goods.order_by("price")

    childList =[]
    for foo in child.split("#"):
        ft = foo.split(":")
        obj = {"name":ft[0],
               "id":ft[1]}
        childList.append(obj)

    data = {
        "title": "闪购超市",
        "foodtypes": foodtypes,
        "goods": goods,
        "typeid": int(typeid),
        "childList": childList,
        "childid": childid,
        "orderby": orderby,

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