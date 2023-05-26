from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app1 import models
import time


# 登录
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    # 获取用户提交的用户名和密码
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    # 检查用户名、密码是否为空
    if name == "":
        return render(request, "login.html", {"name_error": "用户名不能为空"})
    if pwd == "":
        return render(request, "login.html", {"pwd_error": "密码不能为空"})
    # 检查用户名、密码长度是否合法
    if len(name) > 20:
        return render(request, "login.html", {"name_error": "用户名长度不能超过20个字符"})
    if len(pwd) > 20:
        return render(request, "login.html", {"pwd_error": "密码长度不能超过20个字符"})
    # 检查用户名是否已存在
    user = models.UsersInfo.objects.filter(name=name, pwd=pwd)
    if not user:
        return render(request, "login.html", {"pwd_error": "用户名或密码错误"})
    return redirect("/manage/")


