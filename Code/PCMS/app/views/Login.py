from django.shortcuts import render, HttpResponse, redirect
from django import forms
from Code.PCMS.app import models
import time


# 登录
class LoginForm(forms.Form):
    name = forms.CharField(label="用户名",
                           widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入用户名"}),
                           required=True)
    pwd = forms.CharField(label="密码",
                          widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码"}),
                          required=True)


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        login_check = models.UsersInfo.objects.filter(name=name, pwd=pwd).first
        if not login_check:
            form.add_error("pwd", "用户名或密码错误")
            return render(request, "login.html", {'form': form})
        return HttpResponse("ok")
    return render(request, "login.html", {'form': form})
