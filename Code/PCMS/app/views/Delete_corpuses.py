from django.shortcuts import render, redirect
from Code.PCMS.app import models
from Code.PCMS.app import corpusmanager


def delete_corpuses(request):
    id = request.GET.get('id')
    file_to_delete=models.CorpusInfo.objects.filter(id=id).first().name+".csv"
    models.CorpusInfo.objects.filter(id=id).delete()
    print(file_to_delete)
    manager = corpusmanager.ParallelCorpusManager()
    manager.delete_corpus(file_to_delete)
    return redirect("/manage/")
