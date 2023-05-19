from django.db import models

# Create your models here.

class Chy(models.Model):
    name = models.CharField(verbose_name="语料库名", max_length=20)
    create_time = models.DateTimeField(verbose_name="创建时间")


class UsersInfo(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=20)
    pwd = models.CharField(verbose_name="密码", max_length=20)

