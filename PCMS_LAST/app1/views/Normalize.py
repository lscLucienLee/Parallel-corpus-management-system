from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.normalize import TextNormalizer
from app1 import models


# 修改语料库名
def normalize(request):
    corpus_filename = fileL + now.CORPUS + ".csv"
    normalizer = TextNormalizer(corpus_filename)
    normalizer.process_csv()
    now_corpus = models.CorpusInfo.objects.filter(name=now.CORPUS_NAME).first()
    nid = now_corpus.id
    operate_url = "/operate/?nid=" + str(nid) + "&corpus_name=" + now.CORPUS_NAME
    return redirect(operate_url)
