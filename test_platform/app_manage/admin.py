from django.contrib import admin
from app_manage.models import Project
from app_manage.models import Module
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['name', 'status', 'describe', 'create_time', 'update_time']
    # 搜索框
    search_fields = ['name']
    # 筛选器
    list_filter = ['status']

class ModuleAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['name','describe', "create_time", "project"]
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)