from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, HttpResponse
from app1 import models
from app1.tools.txttocsv import TxtToCsvConverter
from app1.views.Nowinfo import now, fileL, fileS
import time
from app1.tools import corpusmanager, corpusadd

corpuses = []
index = 0
max_index = 0

import_file = ""


def input_add(request):
    return render(request, "input.html")


def manual_create(request):
    global index
    global max_index
    # 获取语料库名称
    corpus_name = request.POST.get("corpus_name")
    # 语料库名称不能为空
    if corpus_name == "":
        if index == 0:
            return render(request, "create_hand.html", {"corpus_name_null": "语料库名称不能为空！"})
        else:
            return render(request, "create_hand.html",
                          {"corpus_name_null": "语料库名称不能为空！", "left": corpuses[index],
                           "right": corpuses[index + 1]})
    else:
        if index != max_index:
            return render(request, "create_hand.html",
                          {"corpus_name": corpus_name, "corpus_name_null": "请回到最后一条创建"})
        else:
            corpuses.insert(index, request.POST.get("left"))
            corpuses.insert(index + 1, request.POST.get("right"))
            index += 2
            max_index += 2
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            models.CorpusInfo.objects.create(user=now.USER, name=corpus_name, create_time=create_time)
            manager = corpusmanager.ParallelCorpusManager()
            # 创建一个平行语料库CSV文件
            csv_file_name = fileL + now.USER + "_" + corpus_name + ".csv"
            manager.create_corpus_csv(csv_file_name)
            # 添加语料
            corpus = corpusadd.AddCorpus(csv_file_name)
            i = 0
            while i < max_index:
                corpus.add_corpus(corpuses[i], corpuses[i + 1])
                i += 2
            # 获取数据库中所有的语料库信息
            return redirect("/manage/")


def last_or_next(request):
    choice = request.GET.get("choice")
    corpus_name = request.POST.get("corpus_name")
    global index
    global max_index
    # 用户点击的是“上一条”
    if choice == "0":
        if index == 0:
            print(corpuses)
            print(index)
            return render(request, "input.html",
                          {"left": corpuses[index], "right": corpuses[index + 1],
                           "corpus_name": corpus_name})  # 如果是第一条，点击无效
        else:
            # 保存用户输入
            if index == max_index:
                corpuses.insert(index, request.POST.get("left"))
                corpuses.insert(index + 1, request.POST.get("right"))
            else:
                corpuses[index] = request.POST.get("left")
                corpuses[index + 1] = request.POST.get("right")
            index -= 2
            print(corpuses)
            print(index)
            return render(request, "input.html",
                          {"left": corpuses[index], "right": corpuses[index + 1], "corpus_name": corpus_name})
    # 用户点击的是“下一条”
    elif choice == "1":
        left = request.POST.get("left")
        right = request.POST.get("right")
        # 检查语料框是否为空
        if left == "":
            print(corpuses)
            print(index)
            return render(request, "input.html",
                          {"left_null": "左语料为空！", "left": left, "right": right, "corpus_name": corpus_name})
        if right == "":
            print(corpuses)
            print(index)
            return render(request, "input.html",
                          {"right_null": "右语料为空！", "left": left, "right": right, "corpus_name": corpus_name})
        # 保存用户输入
        if index == max_index:
            corpuses.insert(index, request.POST.get("left"))
            corpuses.insert(index + 1, request.POST.get("right"))
        else:
            corpuses[index] = request.POST.get("left")
            corpuses[index + 1] = request.POST.get("right")
        index += 2
        if index > max_index:
            max_index = index
            print(corpuses)
            print(index)
            return render(request, "input.html", {"corpus_name": corpus_name})
        else:
            print(corpuses)
            print(index)
            return render(request, "input.html",
                          {"left": corpuses[index], "right": corpuses[index + 1], "corpus_name": corpus_name})


def file_create(request):
    return render(request, "import.html")


def upload_import_file(request):
    global import_file
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        name = request.POST.get("name")
        fs = FileSystemStorage()
        import_file = fileS + uploaded_file.name
        fs.save(fileS + uploaded_file.name, uploaded_file)
        save_file = fileL + now.USER + "_" + name + ".csv"
        converter = TxtToCsvConverter(import_file, save_file)
        converter.convert()
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        models.CorpusInfo.objects.create(user=now.USER, name=name, create_time=create_time)
        return redirect("/manage/")
