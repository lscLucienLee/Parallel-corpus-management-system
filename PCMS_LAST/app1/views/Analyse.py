from django.shortcuts import render, HttpResponse, redirect
from app1.views.Nowinfo import now, fileL
from app1.tools.analyzer import CorpusAnalyzer
from app1 import models
import json
import pdb


# 修改语料库名
def analyse(request):
    return render(request, "analyse.html", {"corpus_name": now.CORPUS_NAME})


def analyse_data(request):
    corpus_filename = fileL + now.CORPUS + ".csv"
    analyzer = CorpusAnalyzer(corpus_filename)
    analysis_result = analyzer.analyze_corpus()
    total = analysis_result["total_sentences"]
    top = analysis_result["top_five_words"]
    data = [{"corpus_number": total}]
    rank = 1
    for obj in top:
        data.append({"id": rank, "translation": obj[0], "frequencyId": obj[1]})
        rank = rank + 1
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return HttpResponse(data)


def analyse_search(request):
    search_word = request.POST.get("word")
    print("search_word:" + search_word)
    corpus_filename = fileL + now.CORPUS + ".csv"
    analyzer = CorpusAnalyzer(corpus_filename)
    word_frequency = analyzer.search_word_frequency(search_word)
    print(word_frequency)
    data = {
        "word": str(search_word),
        "frequencyId": str(word_frequency)
    }
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data)
