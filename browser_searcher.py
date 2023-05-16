import csv
import json
from datetime import datetime

class CorpusBrowser:
    def __init__(self, corpus_name):
        self.corpus_name = corpus_name

    def view_corpus(self):
        with open(self.corpus_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            content = [row for row in reader]
        return content

class CorpusSearcher:
    def __init__(self, corpus_name):
        self.corpus_name = corpus_name
        self.browser = CorpusBrowser(corpus_name)

    def search(self, keyword):
        content = self.browser.view_corpus()
        search_results = [row for row in content if keyword in row[1] or keyword in row[2]]
        return search_results

    def export_results(self, results, export_format='csv'):
        if export_format == 'txt':
            filename = f'search_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            with open(filename, 'w', encoding='utf-8') as f:
                for row in results:
                    f.write(json.dumps(row, ensure_ascii=False) + '\n')
        elif export_format == 'csv':
            filename = f'search_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(results)

# if __name__ == "__main__":
#     corpus_name = "your_corpus.csv"
#     searcher = CorpusSearcher(corpus_name)
#     keyword = "your_keyword"
#     search_results = searcher.search(keyword)

#     # 输出查询结果
#     print(search_results)

#     # 导出查询结果到文本文件
#     searcher.export_results(search_results, 'txt')

#     # 导出查询结果到CSV文件
#     searcher.export_results(search_results, 'csv')
