from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app1 import models
import time


def update(request):
    if request.method == "GET":
        corpus = request.GET.get('corpus')
        nid = request.GET.get('id')
        user = corpus.split('_')[1]
        corpus_name = corpus.split('_')[2]
        olddata = corpus_search(corpus=corpus, id=id)
        return render(request, "update.html", {"olddata": olddata}, {"corpus_name": corpus_name})
    original = request.POST.get("original")
    translation = request.POST.get("translation")
    corpus_update(corpus=corpus, nid=id, original=original, translation=translation)
    browse_url = "/browse/" + "?corpus_name=" + corpus_name + "&user=" + user
    return redirect(browse_url)


class ParallelCorpus:
    def __init__(self, filename):
        self.filename = filename

    def search_corpus(self, keyword):
        matching_rows = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if keyword in row["text1"] or keyword in row["text2"]:
                    matching_rows.append({"id": row["id"], "text1": row["text1"], "text2": row["text2"]})
        return matching_rows
