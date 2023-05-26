import csv
import re
from datetime import datetime

class CorpusNormalizer:
    def __init__(self, corpus_file_path):
        self.corpus_file_path = corpus_file_path
        self.log_file = "corpus_normalization_log.txt"
        
    def normalize_corpus(self):
        with open(self.corpus_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            content = [row for row in reader]
        
        normalized_content = self.normalize_content(content)
        
        with open(self.corpus_file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(normalized_content)
        
        self.log_operation()
    
    def normalize_content(self, content):
        normalized_content = []
        for row in content:
            normalized_row = []
            for text in row:
                normalized_text = self.normalize_text(text)
                normalized_row.append(normalized_text)
            normalized_content.append(normalized_row)
        return normalized_content
    #这里只对空格和逗号进行了规范化
    def normalize_text(self, text):
        text = re.sub(r'\s', ' ', text)  # Replace all whitespace characters with a standard space
        text = re.sub(r',', ',', text)  # Replace all types of commas with a standard comma
        return text
    
    def log_operation(self):
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"Normalization operation on corpus '{self.corpus_file_path}' started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Normalization operation on corpus '{self.corpus_file_path}' finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

# if __name__ == "__main__":
#     corpus_file_path = "your_corpus.csv"
#     normalizer = CorpusNormalizer(corpus_file_path)
#     normalizer.normalize_corpus()
