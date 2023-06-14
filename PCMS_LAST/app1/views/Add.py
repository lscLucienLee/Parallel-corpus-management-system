from django.shortcuts import render, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.corpusadd import AddCorpus


# 添加语料
def add(request):
    if request.method == "GET":
        return render(request, "add.html", {"corpus_name": now.CORPUS_NAME})
    original = request.POST.get("original")
    translation = request.POST.get("translation")
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus = AddCorpus(corpus_filename)
    corpus.add_corpus(original, translation)
    browse_url = "/browse/?corpus_name=" + now.CORPUS_NAME
    return redirect(browse_url)
