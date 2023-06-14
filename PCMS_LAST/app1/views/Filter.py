from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.filter import CorpusFilter
from app1 import models


# 修改语料库名
def filter(request):
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus = CorpusFilter(corpus_filename)
    corpus.filter_corpus()
    now_corpus = models.CorpusInfo.objects.filter(name=now.CORPUS_NAME).first()
    nid = now_corpus.id
    operate_url = "/operate/?nid=" + str(nid) + "&corpus_name=" + now.CORPUS_NAME
    return redirect(operate_url)
