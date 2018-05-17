from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
def register(request):
    return render(request,'ds_user/register.html')

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0, 'error_pwd':0, 'uname':uname}
    return render(request,'ds_user/login.html', context)

def login_handle(request):
    #接收请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    #根据用户名查询对象
    users=UserInfo.objects.filter(uname=uname)
    print(uname)
    if len(users)==1:
        s1=sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            #记住用户名
            if jizhu !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title':'用户登录','error_name':0, 'error_pwd':1, 'uname':uname, 'ipwd':upwd}
            return render(request, 'ds_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'ipwd': upwd}
        return render(request, 'ds_user/login.html', context)

def info(request):
    user_email= UserInfo.objects.get(id=request.session['user_id']).uemail
    context={
        'title':'用户中心',
        'user_email':user_email,
        'user_name':request.session['user_name']}
    return render(request, 'ds_user/info.html', context)

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def register_handle(request):
    #接受用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('user_pwd').encode('utf-8')
    uemail=post.get('user_email')
    uphone=post.get('user_phone')
    # return render(request,'ds_user/register.html')

    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd=s1.hexdigest()

    #创建对象
    user = UserInfo()
    user.uname= uname
    user.upwd= upwd
    user.uemail= uemail
    user.uphone= uphone
    user.save()
    #注册成功，转到登录页面
    return redirect('../login/')

def wishlist(request):
    return render(request, 'ds_user/wishlist.html')