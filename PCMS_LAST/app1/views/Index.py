import json

from django.shortcuts import render, redirect, HttpResponse

from app1 import models
from app1.tools.analyzer import CorpusAnalyzer
from app1.tools.auto_evaluation import autoTranslationEvaluator
from app1.tools.filter import CorpusFilter
from app1.tools.manul_evaluation import TranslationComparison
from app1.tools.normalize import TextNormalizer
from app1.tools.remove import CorpusRemover
from app1.views.Nowinfo import now, fileL
from app1.tools.corpussplit import CorpusSplitter
from app1.tools.corpusmerge import CorpusMerger
from app1.tools.corpussearch import ParallelCorpus


def index(request):
    data = request.POST.get("corpus_name")
    print(data)
    return


def indexx(request):
    splitter = CorpusSplitter()
    corpus_filename1 = fileL + "666.csv"
    corpus_filename2 = fileL + "777.csv"
    split_infos = [
        {'ratio': 3, 'output_name': corpus_filename1},
        {'ratio': 4, 'output_name': corpus_filename2},
    ]
    corpus_filename = fileL + "chy_999.csv"
    splitter.split_corpus(corpus_filename, *split_infos)
    return HttpResponse("OK")


def indexxxx(request):
    search_key = "你"
    corpus_filename = fileL + "chy_977.csv"
    corpus = ParallelCorpus(corpus_filename)
    queryset = corpus.search_corpus(search_key)
    print(queryset)
    return HttpResponse("OK")


# # 使用示例
# splitter = CorpusSplitter()

# # 拆分平行语料库CSV文件
# split_infos = [
#     {'ratio': 3, 'output_name': 'split_corpus1.csv'},
#     {'ratio': 4, 'output_name': 'split_corpus2.csv'},
# ]

# splitter.split_corpus('corpus.csv', *split_infos)

def indexxx(request):
    merger = CorpusMerger()
    corpus_filename1 = fileL + "567.csv"
    corpus_filename2 = fileL + "123.csv"
    corpus_filename3 = fileL + "345.csv"
    merger.merge_corpora(corpus_filename1, corpus_filename2, corpus_filename3)
    return HttpResponse("OK")


# # 使用示例
# merger = CorpusMerger()

# # 合并多个平行语料库CSV文件
# merger.merge_corpora('merged_corpus.csv', 'corpus1.csv', 'corpus2.csv', 'corpus3.csv')


def iindex(request):
    corpus_filename = fileL + "chy_1.csv"
    corpus = CorpusFilter(corpus_filename)
    corpus.filter_corpus()
    return HttpResponse("OK")


def iiindex(request):
    corpus_filename = fileL + "chy_3.csv"
    corpus_handler = CorpusRemover(corpus_filename)
    deduplicated_corpus = corpus_handler.remove_duplicates()
    for data in deduplicated_corpus:
        print("已删除的重复数据：" + str(data))
    return HttpResponse("OK")


def iiiindex(request):
    corpus_filename = fileL + "chy_3.csv"
    normalizer = TextNormalizer(corpus_filename)
    normalizer.process_csv()
    return HttpResponse("OK")


def outo(request):
    corpus_filename1 = fileL + "test.csv"
    corpus_filename2 = fileL + "machine_test.csv"
    evaluator = autoTranslationEvaluator(corpus_filename1, corpus_filename2)
    avg_score = evaluator.evaluate_translations()
    print(f"整个文件的平均得分: {avg_score}")
    return HttpResponse("OK")


# # 使用示例
# evaluator = autoTranslationEvaluator("corpus.csv", "machine_translations.csv")
# avg_score = evaluator.evaluate_translations()
# print(f"整个文件的平均得分: {avg_score}")

# def ana(request):
#     corpus_filename = fileL + "chy_999.csv"
#     corpus_analyzer = CorpusAnalyzer(corpus_filename)
#     results = corpus_analyzer.analyze_corpus()
#     print(results)
#     return HttpResponse("OK")

def ana(request):
    corpus_file = fileL + "chy_999.csv"
    grade_file = "D:\\py code\\PCMS\\app1\\scratchFiles\\machine_test.csv"
    comparer = TranslationComparison(corpus_file, grade_file)
    comparison_data = comparer.compare_translations()
    print(comparison_data)
    data = json.dumps(comparison_data, ensure_ascii=False)
    return HttpResponse(data)
