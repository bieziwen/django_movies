import re
import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

#重定向
#render 相当于本界面刷新
# Create your views here.
from django.template import loader

from apps.account.models import User
from django_movies import settings


def test2(request):
    return HttpResponse('呵呵呵')




#第一种情况直接访问登录界面
#第二种 做验证的时候会跳转到登录界面？next=/account/login/
def login_view(request):
    if request.method=='GET':
        next=request.GET.get('next')
        return render(request,'login.html',{'next':next})
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        users=User.objects.filter(username=username)
        user=authenticate(username=username,password=password)
        #上面验证用户名密码是否正确
        #判断用户是否激活
        if users:
            is_uname=users.first()
            if is_uname.is_active==0:
                is_active=0
                return render(request, 'login.html', {'msg': '您的账号未激活！','user':user,'is_active':is_active})
        try:
            if user.is_active:
                #         登录成功
                #         记录登录状态
                login(request, user)

                return redirect('/home/index')
            else:
                return render(request, 'login.html',{{'msg':'您的账号未激活！'}})
        except:
            return render(request,'login.html',{'user':user,'msg':'用户名或密码不存在'})

#发送邮件激活
#注册通过之后 is_active=0
#发送邮件
#用户点击激活连接
#访问服务器指定的接口（激活的接口）
#修改当前用户的激活状态 is_active=1
def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            email=request.POST.get('email')
            if username and password and phone:
                #  注册
                user = User.objects.filter(Q(username=username) | Q(phone=phone))

                if user.exists():
                    print('用户名或者手机号已存在！！')
                else:
                    # 保存用户的操作
                    user = User.objects.create_user(username=username, password=password, phone=phone,is_active=0)
                    if user:
                        # 如果注册成功 直接记住用户登录状态，跳转首页
                        #            跳转登录页面，让用户再登录一次
                        # 记住用户状态
                        # 底层做了两个操作：
                        # 第一个将用户信息保存到session中
                        # 第二个操作将用户信息绑定到request对象上
                        # login(request, user)
                        # 可以通过request.user拿到用户信息
                        #设置有效期  redis
                        tooken=1
                        #随机生成字符串
                        # tooken=uuid.uuid4()
                        # cache.set(tooken,user.id,timeout=10*60)
                        # active_url=f'http://127.0.0.1:8000/account/active/?uid=tooken'
                        active_url=f'http://127.0.0.1:8000/account/active/?uid={user.id}'
                        content = loader.render_to_string('mail.html', request=request,context={'username':username,'active_url':active_url})
                        send_active_mail(subject='91Pro电影会员注册',msg=content,to=[email])
                        login(request, user)
                        return redirect('/account/login/')
                    else:
                        return render(request,'login.html',)
        except:
            return render(request,'404.html')


@login_required(login_url='/account/login/')
def logout_view(request):
    #退出登录
    logout(request)
    return redirect('/home/index')

#验证用户是否登录
@login_required(login_url='/account/login/')
def update(request,password):
    user=request.user
    user.password=password
    user.save()
    return redirect('/')


def detail(request):
    pass


def hello_mail(request):
    """
    subject  标题
    message  邮件的内容
    from_email  发送者
    recipient_list  接受者（列表）
    html_message  邮件内容以HTML格式显示


    :param request:
    :return:
    """
    content = loader.render_to_string('mail.html',request=request)
    send_mail(subject='91pro电影网',
              message='注册成功可以观看更多高清无码视频',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['18614068889@163.com']


              )
    return render(request,'msg')

def send_active_mail(subject,msg,to):
    send_mail(subject=subject,
              message='',
              html_message=msg,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )


#http://127.0.0.1:8000/account/active/?uid=1
def user_active(request):
    uid=request.GET.get('uid')
    # tooken=request.GET.get('uid')
    # uid=cache.get(tooken)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        is_active = 1
        home='http://127.0.0.1:8000/account/login/'
        return render(request,'active_success.html',{'is_active':is_active,'home':home})
    else:
        return redirect('/account/inactive')

def login_active(request):
    if request.method == 'GET':
        # url='http://127.0.0.1:8000/account/inactive/'
        return render(request, 'login_ative.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email=request.POST.get('email')
        user = User.objects.filter(Q(username=username) | Q(email=email))
        id=user.first().id
        if user:
            active_url = f'http://127.0.0.1:8000/account/active/?uid={id}'
            content = loader.render_to_string('mail.html', request=request,
                                          context={'username': username, 'active_url': active_url})
            send_active_mail(subject='91Pro电影会员注册', msg=content, to=[email])
            return redirect('/account/login/')
        else:
            return HttpResponse('用户名或者邮箱不匹配')
