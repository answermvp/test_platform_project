from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
# Create your views here.


# 装饰需要用户登陆状态的视图
@login_required
def manage(request):
    """项目管理"""
    project_list = Project.objects.all()
    return render(request, 'manage.html', {'projects': project_list})
