from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app1 import models
import time

global corpus_name
global user
global corpus
global nid


def correct(request):
    if request.method == "GET":
        corpus_name = request.GET.get('corpus_name')
        user = request.GET.get('user')
        nid = request.GET.get('id')
        corpus = user + "_" + corpus_name

        olddata = models.CorpusInfo.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {"olddata": olddata})

    newname = request.POST.get("newname")
    # 数据库中更改
    models.CorpusInfo.objects.filter(id=nid).update(name=newname)
    # 更改文件名
    newcorpus = user + "_" + newname
    renamefile(corpus, newcorpus)

    manage_url = "/manage/" + "?user=" + user
    return redirect(manage_url)


def cor(request):
    if request.method == "GET":
        corpus_name = request.GET.get('corpus_name')
        user = request.GET.get('user')
        nid = request.GET.get('id')
        corpus = user + "_" + corpus_name

        olddata = models.CorpusInfo.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {"olddata": olddata})

    newname = request.POST.get("newname")
    # 数据库中更改
    models.CorpusInfo.objects.filter(id=nid).update(name=newname)
    # 更改文件名
    newcorpus = user + "_" + newname
    renamefile(corpus, newcorpus)

    manage_url = "/manage/" + "?user=" + user
    return redirect(manage_url)
