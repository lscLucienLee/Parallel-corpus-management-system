import json
import os

from django.http import HttpResponse, JsonResponse, FileResponse, Http404
from django.shortcuts import render, redirect

from app1.tools.align import FastAlignWrapper
from app1.views.Nowinfo import now, fileL, fileS
from app1.tools.corpusadd import AddCorpus

num = -1
get_data = []
data_align = []


# 添加语料
def align(request):
    global num
    if request.method == "GET":
        num = -1
        return render(request, "align.html", {"corpus_name": now.CORPUS_NAME})


def align_data(request):
    global num, data_align
    num = num + 1
    fast_align_path = '..PCMS\\app1\static\plugins\\fast_align\\fast_align.exe'  # fast_align.exe 路径
    corpus_name = now.CORPUS
    aligner = FastAlignWrapper(corpus_name, fast_align_path)
    data_align = aligner.align_words()
    send = json.dumps(data_align[num], ensure_ascii=False)
    return HttpResponse(send)


def align_next(request):
    global num
    num = num + 1
    if num == 5:
        error = {"error": "已经到达最后一条"}
        return JsonResponse(error)
    data = request.POST.get("data")
    print(data)
    global get_data
    get_data.append(data)
    print(get_data)
    send = json.dumps(data_align[num], ensure_ascii=False)
    return HttpResponse(send)


def download_align_file(request, file_name):
    file_path = fileS + file_name
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = FileResponse(open(file_path, 'rb'), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    raise Http404("文件不存在！")
