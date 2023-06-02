from django.shortcuts import render, redirect
from Code.PCMS.app import models
import time
from Code.PCMS.app.views.Last_or_next import corpuses


def create(request):
    global index
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
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        models.CorpusInfo.objects.create(name=corpus_name, create_time=create_time)
        # 获取数据库中所有的语料库信息
        CorpusInfo_list = models.CorpusInfo.objects.all()
        return render(request, "manage.html", {"CorpusInfo_list": CorpusInfo_list})
