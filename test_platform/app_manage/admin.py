from django.contrib import admin
from app_manage.models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['name', 'status', 'describe', 'create_time', 'update_time']
    # 搜索框
    search_fields = ['name']
    # 筛选器
    list_filter = ['status']


admin.site.register(Project, ProjectAdmin)