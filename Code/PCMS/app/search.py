import csv

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

# 示例用法
corpus = ParallelCorpus("your_corpus_filename.csv")
result = corpus.search_corpus("关键词")
print(result)
