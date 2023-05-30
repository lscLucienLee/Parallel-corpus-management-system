from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app1 import models
import time


# 浏览查询


def browse(request):
    if request.method == "GET":
        # 当前语料库
        corpus_name = request.GET.get('corpus_name')
        user = request.GET.get('user')
        corpus = user + "_" + corpus_name

        queryset = getcorpus(corpus)
        return render(request, "browse.html", {'queryset': queryset}, {'corpus': corpus}, {'corpus_name': corpus_name},
                      {'user': user})
    key = request.POST.get("key")
    queryset = corpus_search(corpus_name, key)
    return render(request, "user.html", {'queryset': queryset})


def delete_corpus(request):
    # 语料删除
    corpus = request.GET.get('corpus')
    id = request.GET.get('id')
    corpus_delete(corpus, id)
    user = corpus.split('_')[1]
    corpus_name = corpus.split('_')[2]
    browse_url = "/browse/" + "?corpus_name=" + corpus_name + "&user=" + user
    return redirect(browse_url)


def browse(request):
    return render(request, "browse.html")
