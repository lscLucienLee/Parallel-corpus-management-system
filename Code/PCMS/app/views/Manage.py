from django.shortcuts import render, redirect
from Code.PCMS.app import models


def manage(request):
    # 获取数据库中所有的语料库信息
    CorpusInfo_list = models.CorpusInfo.objects.all()
    return render(request, "manage.html", {"CorpusInfo_list": CorpusInfo_list})
