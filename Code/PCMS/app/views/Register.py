from django.shortcuts import render, redirect
from Code.PCMS.app import models


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    # 获取用户提交的用户名和密码
    name = request.POST.get("user")
    pwd = request.POST.get("pwd")
    # 检查用户名、密码是否为空
    if name == "":
        return render(request, "register.html", {"user_error": "用户名不能为空"})
    if pwd == "":
        return render(request, "register.html", {"pwd_error": "密码不能为空"})
    # 检查用户名、密码长度是否合法
    if len(name) > 20:
        return render(request, "register.html", {"user_error": "用户名长度不能超过20个字符"})
    if len(pwd) > 20:
        return render(request, "register.html", {"pwd_error": "密码长度不能超过20个字符"})
    # 检查用户名是否已存在
    user_list = models.UsersInfo.objects.all()
    for item in user_list:
        if name == item.name:
            return render(request, "register.html", {"user_error": "用户名已存在"})
    # 将数据添加到数据库
    models.UsersInfo.objects.create(name=name, pwd=pwd)
    return redirect("/login/")