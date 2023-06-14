from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1 import models


# 修改语料库名
def operate(request):
    if request.method == "GET":
        now.CORPUS_NAME = request.GET.get('corpus_name')
        now.CORPUS = now.USER + "_" + now.CORPUS_NAME
        return render(request, "operate.html", {"corpus_name": now.CORPUS_NAME})

