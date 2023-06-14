import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.tools.corpusmerge import CorpusMerger
from app1.views.Nowinfo import now, fileL
from app1 import models
import json

corpus_s = []


def merge(request):
    global corpus_s
    if request.method == "GET":
        return render(request, "merge.html")
    corpus_name = request.POST.get("new_corpus_name")
    new_corpus = fileL + now.USER + "_" + corpus_name + ".csv"
    corpus_names = []
    for item in corpus_s:
        corpus_names.append(fileL + now.USER + "_" + item + ".csv")
    merger = CorpusMerger()
    merger.merge_corpora(new_corpus, *corpus_names)
    print(corpus_name)
    return redirect("/manage/")


def merge_corpus_name(request):
    global corpus_s
    data = request.POST.get("data")
    print(data)
    corpus_s = json.loads(data)
    return HttpResponse()


def merge_data(request):
    CorpusInfo_list = models.CorpusInfo.objects.filter(user=now.USER)
    data = []
    for item in CorpusInfo_list:
        new_time = str(item.create_time)
        new_time = new_time.split('+')[0]
        new_time = new_time.replace('T', ' ')
        new_time = new_time.replace('Z', ' ')
        data.append(
            {"nid": str(item.id), "name": str(item.name), "time": new_time})
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data)
