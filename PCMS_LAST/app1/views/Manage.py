from django.shortcuts import render, HttpResponse, redirect
from app1 import models
from app1.views.Nowinfo import now, fileL
from app1.tools.corpusmanager import ParallelCorpusManager
import json


def manage(request):
    return render(request, "manage.html")


def manage_data(request):
    # 获取数据库中该用户所有的语料库信息
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


def delete_corpuses(request):
    now.CORPUS_NAME = request.GET.get('corpus_name')
    now.CORPUS = now.USER + "_" + now.CORPUS_NAME
    nid = request.GET.get('nid')
    # 数据库中删除
    models.CorpusInfo.objects.filter(id=nid).delete()
    # 删除语料库文件
    corpus_filename = fileL + now.CORPUS + ".csv"
    manager = ParallelCorpusManager()
    manager.delete_corpus(corpus_filename)
    return redirect("/manage/")
