import csv


class ParallelCorpus:
    def __init__(self, filename):
        self.filename = filename

    def search_corpus(self, keyword):
        matching_rows = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if keyword in row["original"] or keyword in row["translation"]:
                    matching_rows.append(
                        {"id": row["id"], "original": row["original"], "translation": row["translation"]})
        return matching_rows


class ParallelCorpus_id:
    def __init__(self, filename):
        self.filename = filename

    def search_corpus_id(self, keyword):
        matching_rows = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if keyword in row["id"]:
                    matching_rows.append(
                        {"id": row["id"], "original": row["original"], "translation": row["translation"]})
        return matching_rows

# 示例用法
# corpus = ParallelCorpus("your_corpus_filename.csv")
# result = corpus.search_corpus("关键词")
# print(result)
