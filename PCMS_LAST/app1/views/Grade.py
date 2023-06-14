from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse, redirect

from app1.tools.auto_evaluation import autoTranslationEvaluator
from app1.tools.manul_evaluation import TranslationComparison
from app1.views.Nowinfo import now, fileL, fileS
from app1 import models
import json

manual_file = ""
auto_file = ""


def grade(request):
    return render(request, "grade.html", {"corpus_name": now.CORPUS_NAME})


def manual_eval(request):
    return render(request, "tran_manual_eval.html", {"corpus_name": now.CORPUS_NAME})


def auto_eval(request):
    return render(request, "tran_auto_eval.html", {"corpus_name": now.CORPUS_NAME})


def upload_manual_file(request):
    global manual_file
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        manual_file = fileS + uploaded_file.name
        fs.save(fileS + uploaded_file.name, uploaded_file)
        return redirect("/grade/")


def upload_auto_file(request):
    global auto_file
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        auto_file = fileS + uploaded_file.name
        fs.save(fileS + uploaded_file.name, uploaded_file)
        # return redirect("/auto/")
        print(uploaded_file)
        return redirect("/auto/")


def grade_data(request):
    global manual_file
    corpus_file = fileL + now.CORPUS + ".csv"
    comparer = TranslationComparison(corpus_file, manual_file)
    comparison_data = comparer.compare_translations()
    print(comparison_data)
    data = []
    i = 1
    for item in comparison_data:
        data.append({
            "id": str(i),
            "original": item['original'],
            "standard_translation": item['standard_translation'],
            "machine_translation": item['machine_translation']
        })
        i = i + 1
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return HttpResponse(data)


def auto_data(request):
    global auto_file
    print("正在自动评价" + str(auto_file))
    corpus_file = fileL + now.CORPUS + ".csv"
    evaluator = autoTranslationEvaluator(corpus_file, auto_file)
    avg_score = evaluator.evaluate_translations()
    print(f"整个文件的平均得分: {avg_score}")
    avg_score = round(avg_score, 2)
    return HttpResponse(avg_score)
