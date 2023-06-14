import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.views.Nowinfo import now, fileL
from app1 import models
from app1.tools.corpussplit import CorpusSplitter
import json
import pdb

divided_corpus_name = None


def divide(request):
    global divided_corpus_name
    if request.method == "GET":
        return render(request, "divide.html")
    num = int(request.POST.get("num")) + 1
    if num == 2:
        rat0 = int(request.POST.get("rat0"))
        rat1 = int(request.POST.get("rat1"))
        name0 = str(request.POST.get("name0"))
        name1 = str(request.POST.get("name1"))
        corpus_filename0 = fileL + now.USER + "_" + name0 + ".csv"
        corpus_filename1 = fileL + now.USER + "_" + name1 + ".csv"
        split_infos = [
            {"ratio": rat0, "output_name": corpus_filename0},
            {"ratio": rat1, "output_name": corpus_filename1},
        ]
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        models.CorpusInfo.objects.create(user=now.USER, name=name0, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name1, create_time=create_time)
    if num == 3:
        rat0 = int(request.POST.get("rat0"))
        rat1 = int(request.POST.get("rat1"))
        rat2 = int(request.POST.get("rat2"))
        name0 = str(request.POST.get("name0"))
        name1 = str(request.POST.get("name1"))
        name2 = str(request.POST.get("name2"))
        corpus_filename0 = fileL + now.USER + "_" + name0 + ".csv"
        corpus_filename1 = fileL + now.USER + "_" + name1 + ".csv"
        corpus_filename2 = fileL + now.USER + "_" + name2 + ".csv"
        split_infos = [
            {"ratio": rat0, "output_name": corpus_filename0},
            {"ratio": rat1, "output_name": corpus_filename1},
            {"ratio": rat2, "output_name": corpus_filename2},
        ]
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        models.CorpusInfo.objects.create(user=now.USER, name=name0, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name1, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name2, create_time=create_time)
    if num == 4:
        rat0 = int(request.POST.get("rat0"))
        rat1 = int(request.POST.get("rat1"))
        rat2 = int(request.POST.get("rat2"))
        rat3 = int(request.POST.get("rat3"))
        name0 = str(request.POST.get("name0"))
        name1 = str(request.POST.get("name1"))
        name2 = str(request.POST.get("name2"))
        name3 = str(request.POST.get("name3"))
        corpus_filename0 = fileL + now.USER + "_" + name0 + ".csv"
        corpus_filename1 = fileL + now.USER + "_" + name1 + ".csv"
        corpus_filename2 = fileL + now.USER + "_" + name2 + ".csv"
        corpus_filename3 = fileL + now.USER + "_" + name3 + ".csv"
        split_infos = [
            {"ratio": rat0, "output_name": corpus_filename0},
            {"ratio": rat1, "output_name": corpus_filename1},
            {"ratio": rat2, "output_name": corpus_filename2},
            {"ratio": rat3, "output_name": corpus_filename3},
        ]
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        models.CorpusInfo.objects.create(user=now.USER, name=name0, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name1, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name2, create_time=create_time)
        models.CorpusInfo.objects.create(user=now.USER, name=name3, create_time=create_time)
    for obj in split_infos:
        print(obj)
        name = obj['output_name']
        # create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # models.CorpusInfo.objects.create(user=now.USER, name=name, create_time=create_time)
    print("拆分信息：" + str(split_infos))
    splitter = CorpusSplitter()
    splitter.split_corpus(divided_corpus_name, *split_infos)
    return render(request, "divide.html")


def divide_corpus_name(request):
    global divided_corpus_name
    data = request.POST.get("corpus_name")
    print("被拆分的语料库：" + data)
    divided_corpus_name = fileL + now.USER + "_" + data + ".csv"
    return redirect("/manage/")


def divide_data(request):
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
