import csv
import re

class CorpusFilter:
    def __init__(self, path):
        self.path = path

    def remove_empty_rows(self, data):
        return [row for row in data if row['original'] and row['translation']]

    def remove_html_tags(self, text):
        return re.sub('<[^<]+?>', '', text)

    def process_data(self, data):
        processed_data = []
        for row in data:
            row['original'] = self.remove_html_tags(row['original'])
            row['translation'] = self.remove_html_tags(row['translation'])
            processed_data.append(row)
        return processed_data

    def filter_corpus(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        data = self.remove_empty_rows(data)
        data = self.process_data(data)

        with open(self.path, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'original', 'translation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

# 使用方法：
# 创建CsvFilter类的实例，并提供CSV文件路径
csv_filter = CorpusFilter('your_csv_file_path.csv')
# 调用 filter_csv 方法以过滤并覆盖原CSV文件
csv_filter.filter_corpus()
