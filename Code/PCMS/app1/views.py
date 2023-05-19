from django.shortcuts import render, HttpResponse, redirect
from app1 import models
import time


# Create your views here.
import os
from django.http import JsonResponse
from readdata import IDBtoCSVConverter
from filter import Corpusfilter
from remove import CorpusRemover
from normalize import CorpusNormalizer
from browser_searcher import CorpusBrowser, CorpusSearcher
from analyzer import CorpusAnalyzer
from auto_evaluation import autoTranslationEvaluator
from manul_evaluation import ManualEvaluation
from align import CorpusAligner
from outdata import CSVToMySQL

def process_request(request):
    data = request.GET
    file_path = data.get("file_path")
    order = data.get("order")
    other = data.get("other")

    # 将IDB表转换为CSV文件
    output_csv = os.path.splitext(file_path)[0] + ".csv"
    converter = IDBtoCSVConverter(host='your_host', port=3306, user='your_user', password='your_password', database='your_database', table=file_path)
    converter.convert(output_csv)

    db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1',
    'database': 'your_database_name',
}
    table_name = 'your_table_name'
    csv_to_mysql = CSVToMySQL(db_config, output_csv, table_name)
    if order == "filtrate":
        filter = Corpusfilter(output_csv)
        filted = filter.filter_corpus()
        csv_to_mysql.import_csv_to_mysql(data=filted)
    elif order == "remove":
        remover = CorpusRemover(output_csv)
        removed = remover.remove_duplicates()
        csv_to_mysql.import_csv_to_mysql(data=removed)
    elif order == "normalize":
        normalizer = CorpusNormalizer()
        normalized = normalizer.normalize_corpus()
        csv_to_mysql.import_csv_to_mysql(data=normalized)
    #这个需求不用我解决
    # elif order == "browse":
    #     browser = CorpusBrowser(output_csv)
    elif order == "search":
        searcher = CorpusSearcher(output_csv)
        searched = searcher.search(other)
        csv_to_mysql.import_csv_to_mysql(data=searched)
    elif order == "analyze":
        analyzer = CorpusAnalyzer(output_csv)
        top = analyzer.analyze_corpus()
        find = analyzer.search_word_frequency(other)
        csv_to_mysql.import_csv_to_mysql(data=top)
        csv_to_mysql.import_csv_to_mysql(data=find)
    elif order == "autoevaluation":
        auto = autoTranslationEvaluator(output_csv)
        score = auto.evaluate_translations(other)
        csv_to_mysql.import_csv_to_mysql(data=score)
    elif order == "manualevaluation":
        manual = ManualEvaluation(output_csv)
        data2 = request.GET
        score1 = data.get("scores")
        score2 = manual.evaluate_translations(other,score1)
        csv_to_mysql.import_csv_to_mysql(data=score2)
    elif order == "align":    
        aligner = CorpusAligner(output_csv)
        aligned = aligner.align_corpus()
        csv_to_mysql.import_csv_to_mysql(data=aligned)
        
    else:
        return JsonResponse({"error": "Unsupported order"})

    return JsonResponse({"success": True})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")


def user(request):
    # 用户界面
    queryset = models.Chy.objects.all()
    return render(request, "user.html", {'queryset': queryset})


def user_add(request):
    # 语料库添加
    if request.method == "GET":
        return render(request, "user_add.html")
    name = request.POST.get("name")
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    models.Chy.objects.create(name=name, create_time=create_time)
    return redirect("/user/")


def user_delete(request):
    # 语料库删除
    nid = request.GET.get('nid')
    models.Chy.objects.filter(id=nid).delete()
    return redirect("/user/")


def user_edit(request, nid):
    # 语料库名称修改
    if request.method == "GET":
        oldname = models.Chy.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {"oldname": oldname})
    name = request.POST.get("name")
    models.Chy.objects.filter(id=nid).update(name=name)
    return redirect("/user/")


# ModelForm
from django import forms


class Usermodelformadd(forms.ModelForm):
    class Meta:
        model = models.Chy
        fields = ["name"]
        # widgets = {
        #   "name":forms.TextInput(attrs={"class":"form-control"}),
        #   "create_time": forms.TextInput(attrs={"class": "form-control"}),


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # 循环找到所有插件，添加样式
    for name, field in self.fields.items():
        field.widget.attrs = {"class": "form-control"}


def user_modelformadd(request):
    if request.method == "GET":
        form = Usermodelformadd
        return render(request, 'user_modelformadd.html', {"form": form})
    form = Usermodelformadd(data=request.POST)
    if form.is_valid():
        form.instance.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        form.save()
        return redirect("/user/")
    else:
        return render(request, 'user_modelformadd.html', {"form": form})
