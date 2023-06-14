from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.remove import CorpusRemover
from app1 import models


# 修改语料库名
def remove(request):
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus_handler = CorpusRemover(corpus_filename)
    deduplicated_corpus = corpus_handler.remove_duplicates()
    for data in deduplicated_corpus:
        print("已删除的重复数据：" + str(data))
    now_corpus = models.CorpusInfo.objects.filter(name=now.CORPUS_NAME).first()
    nid = now_corpus.id
    operate_url = "/operate/?nid=" + str(nid) + "&corpus_name=" + now.CORPUS_NAME
    return redirect(operate_url)
