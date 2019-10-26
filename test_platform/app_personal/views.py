from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            return render(request, 'login.html', {'error': '用户名或密码为空'})
        # 判断用户是否存在
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        else:
            # 记录用户登陆状态
            auth.login(request, user)
            return HttpResponseRedirect('/manage/')


# 装饰需要用户登陆状态的视图
@login_required
def manage(request):
    return render(request, 'manage.html')


def logout(request):
    # 退出
    auth.logout(request)
    return HttpResponseRedirect('/login/')
