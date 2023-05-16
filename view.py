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
