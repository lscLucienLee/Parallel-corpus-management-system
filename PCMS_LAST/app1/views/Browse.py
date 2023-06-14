from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from app1.views.Nowinfo import now, fileL
from app1.tools.getcorpus import GetCorpus
from app1.tools.corpusdelete import DeleteCorpus
from app1.tools.corpussearch import ParallelCorpus
import json

# 浏览查询

search_key = ""


def browse(request):
    global search_key
    now.CORPUS_NAME = request.GET.get('corpus_name')
    now.CORPUS = now.USER + "_" + now.CORPUS_NAME
    key = str(request.GET.get('key'))
    if key == "0":
        search_key = ""
    if key == "None":
        search_key = ""
    return render(request, "browse.html", {"key": search_key})


def browse_data(request):
    global search_key
    # 获取语料库内容
    if not search_key:
        corpus_filename = fileL + now.CORPUS + ".csv"
        corpus = GetCorpus(corpus_filename)
        queryset = corpus.get_corpus()
        data = json.dumps(queryset, ensure_ascii=False)
        return HttpResponse(data)
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus = ParallelCorpus(corpus_filename)
    queryset = corpus.search_corpus(search_key)
    data = json.dumps(queryset, ensure_ascii=False)
    return HttpResponse(data)


def browse_search(request):
    global search_key
    flag = 1
    search_key = request.POST.get("word")
    if not search_key:
        flag = 0
    print("search_key:" + search_key)
    browse_json = {
        "name": str(now.CORPUS_NAME),
        "key": str(flag)
    }
    # "/browse/?corpus_name=" + now.CORPUS_NAME + "&key=" + str(flag)
    return JsonResponse(browse_json)


def delete_corpus(request):
    # 语料删除
    nid = request.GET.get('nid')
    print(nid)
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus = DeleteCorpus(corpus_filename)
    corpus.delete_corpus(nid)
    browse_url = "/browse/?corpus_name=" + now.CORPUS_NAME
    return redirect(browse_url)
