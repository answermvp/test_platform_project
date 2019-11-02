from django.db import models

# Create your models here.


class Project(models.Model):
    """项目表"""
    name = models.CharField("项目名称", max_length=100, null=False, default="")
    describe = models.TextField("项目描述", default="")
    status = models.BooleanField("项目状态", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
