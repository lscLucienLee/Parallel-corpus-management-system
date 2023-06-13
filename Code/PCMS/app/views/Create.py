from django.shortcuts import render, redirect
from Code.PCMS.app import models
import time
from Code.PCMS.app.views.Last_or_next import corpuses
from Code.PCMS.app import corpusmanager,corpusadd


def create(request):
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
        if index!=max_index:
            return render(request,"create_hand.html",{"corpus_name":corpus_name,"corpus_name_null":"请回到最后一条创建"})
        else:
            corpuses.insert(index, request.POST.get("left"))
            corpuses.insert(index + 1, request.POST.get("right"))
            index+=2
            max_index+=2
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            models.CorpusInfo.objects.create(name=corpus_name, create_time=create_time)
            manager = corpusmanager.ParallelCorpusManager()
            # 创建一个平行语料库CSV文件
            csv_file_name = corpus_name + ".csv"
            manager.create_corpus_csv(csv_file_name)
            # 添加语料
            corpus = corpusadd.AddCorpus(csv_file_name)
            i = 0
            while i < max_index :
                corpus.add_corpus(corpuses[i], corpuses[i + 1])
                i += 2
            # 获取数据库中所有的语料库信息
            CorpusInfo_list = models.CorpusInfo.objects.all()
            return render(request, "manage.html", {"CorpusInfo_list": CorpusInfo_list})
