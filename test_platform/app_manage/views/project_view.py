from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from app_manage.models import Project
from app_manage.forms import ProjectForm, ProjectEditForm
# Create your views here.


# 装饰需要用户登陆状态的视图
@login_required
def list_project(request):
    """项目管理"""
    username = request.COOKIES.get('user', '')
    project_list = Project.objects.all()
    return render(request, 'project/list.html', {'projects': project_list, 'user': username})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect('/manage/')
    else:
        form = ProjectForm()
        return render(requests, 'project/add.html', {'form':form, 'id':pid})

def edit_project(request, pid):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect('/manage/')    
    else:
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectEditForm()
        return render(request, 'project/edit.html', {'form':form, 'id':pid})

def delete_project(request, pid):
    if request.method == 'GET':
        p = Project.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect('/manage/')
    else:
        return HttpResponseRedirect('/manage/')

