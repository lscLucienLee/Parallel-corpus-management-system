from django.shortcuts import render, HttpResponse, redirect
from app1 import models
import time


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")


def user(request):
    # 用户界面
    queryset = models.Chy.objects.all()
    return render(request, "user.html", {'queryset': queryset})


def user_add(request):
    # 语料库添加
    if request.method == "GET":
        return render(request, "user_add.html")
    name = request.POST.get("name")
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    models.Chy.objects.create(name=name, create_time=create_time)
    return redirect("/user/")


def user_delete(request):
    # 语料库删除
    nid = request.GET.get('nid')
    models.Chy.objects.filter(id=nid).delete()
    return redirect("/user/")


def user_edit(request, nid):
    # 语料库名称修改
    if request.method == "GET":
        oldname = models.Chy.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {"oldname": oldname})
    name = request.POST.get("name")
    models.Chy.objects.filter(id=nid).update(name=name)
    return redirect("/user/")


# ModelForm
from django import forms


class Usermodelformadd(forms.ModelForm):
    class Meta:
        model = models.Chy
        fields = ["name"]


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # 循环找到所有插件，添加样式
    for name, field in self.fields.items():
        field.widget.attrs = {"class": "form-control"}


def user_modelformadd(request):
    if request.method == "GET":
        form = Usermodelformadd
        return render(request, 'user_modelformadd.html', {"form": form})
    form = Usermodelformadd(data=request.POST)
    if form.is_valid():
        form.instance.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        form.save()
        return redirect("/user/")
    else:
        return render(request, 'user_modelformadd.html', {"form": form})
