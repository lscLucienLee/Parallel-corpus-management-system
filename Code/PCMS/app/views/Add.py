from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app1 import models
import time


# 添加语料
class add(request):
    if request.method == "GET":
        corpus = request.GET.get('corpus')
        user = corpus.split('_')[1]
        corpus_name = corpus.split('_')[2]
        return render(request, "add.html", {"corpus_name": corpus_name})
    original = request.POST.get("original")
    translation = request.POST.get("translation")
    corpus_add(corpus=corpus, original=original, translation=translation)
    browse_url = "/browse/" + "?corpus_name=" + corpus_name + "&user=" + user
    return redirect(browse_url)


def add(request):
    if request.method == "GET":
        corpus = request.GET.get('corpus')
        user = corpus.split('_')[1]
        corpus_name = corpus.split('_')[2]
        return render(request, "add.html", {"corpus_name": corpus_name})
    original = request.POST.get("original")
    translation = request.POST.get("translation")
    corpus_add(corpus=corpus, original=original, translation=translation)
    browse_url = "/browse/" + "?corpus_name=" + corpus_name + "&user=" + user
    return redirect(browse_url)
