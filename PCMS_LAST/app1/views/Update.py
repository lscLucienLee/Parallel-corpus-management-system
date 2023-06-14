from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.corpussearch import ParallelCorpus_id
from app1.tools.corpusupdate import UpdateCorpus

nid = None


def update(request):
    global nid
    if request.method == "GET":
        nid = request.GET.get("nid")
        corpus_filename = fileL + now.CORPUS + ".csv"
        corpus = ParallelCorpus_id(corpus_filename)
        # 获取展示原来的信息，在此基础上修改
        olddata = corpus.search_corpus_id(nid)[0]
        return render(request, "update.html", {"olddata": olddata, "corpus_name": now.CORPUS_NAME})
    original = request.POST.get("original")
    translation = request.POST.get("translation")
    corpus_filename = fileL + now.CORPUS + ".csv"
    corpus = UpdateCorpus(corpus_filename)
    # 更新内容
    corpus.update_corpus(nid, original, translation)
    browseurl = "/browse/?corpus_name=" + now.CORPUS_NAME
    return redirect(browseurl)
