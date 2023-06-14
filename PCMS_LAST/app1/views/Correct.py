from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.corpusmanager import ParallelCorpusManager
from app1 import models

nid = None


# 修改语料库名
def correct(request):
    global nid
    if request.method == "GET":
        now.CORPUS_NAME = request.GET.get('corpus_name')
        now.CORPUS = now.USER + "_" + now.CORPUS_NAME
        nid = request.GET.get('nid')
        olddata = models.CorpusInfo.objects.filter(id=nid).first()
        return render(request, "correct.html", {"olddata": olddata})
    newname = request.POST.get("newname")
    # 数据库中更改
    models.CorpusInfo.objects.filter(id=nid).update(name=newname)
    # 更改文件名
    newcorpus = now.USER + "_" + newname + ".csv"
    corpus_filename = fileL + now.CORPUS + ".csv"
    manager = ParallelCorpusManager()
    manager.rename_corpus(corpus_filename, newcorpus)
    return redirect("/manage/")
