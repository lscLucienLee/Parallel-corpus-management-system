import csv
import os

class AddCorpus:
    def __init__(self, filename):
        self.filename = filename

    def add_corpus(self, new_text1, new_text2):
        corpus = []
        last_id = 0
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                corpus.append({"id": row["id"], "original": row["original"], "translation": row["translation"]})
                last_id = int(row["id"])

        new_corpus = {"id": str(last_id + 1), "original": new_text1, "translation": new_text2}
        corpus.append(new_corpus)

        with open(self.filename, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'original', 'translation']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(corpus)

# # 示例用法
# corpus = AddCorpus("your_corpus_filename.csv")
# corpus.add_corpus("新的文本1", "新的文本2")  # 向语料库中添加新的语料
