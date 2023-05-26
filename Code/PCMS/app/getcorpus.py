import csv

class GetCorpus:
    def __init__(self, filename):
        self.filename = filename

    def get_corpus(self):
        corpus = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                corpus.append({"id": row["id"], "text1": row["text1"], "text2": row["text2"]})
        return corpus

# # 示例用法
# corpus = GetCorpus("your_corpus_filename.csv")
# result = corpus.get_corpus()
# print(result)
