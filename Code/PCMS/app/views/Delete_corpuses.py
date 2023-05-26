from django.shortcuts import render, redirect
from Code.PCMS.app import models


def delete_corpuses(request):
    id = request.GET.get('id')
    models.CorpusInfo.objects.filter(id=id).delete()
    return redirect("/manage/")
