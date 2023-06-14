import csv
import os


class UpdateCorpus:
    def __init__(self, filename):
        self.filename = filename

    def update_corpus(self, target_id, updated_text1, updated_text2):
        corpus = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if int(row["id"]) == int(target_id):
                    corpus.append({"id": row["id"], "original": updated_text1, "translation": updated_text2})
                else:
                    corpus.append({"id": row["id"], "original": row["original"], "translation": row["translation"]})

        with open(self.filename, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ["id", "original", "translation"]
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(corpus)

# # 示例用法
# corpus = UpdateCorpus("your_corpus_filename.csv")
# corpus.update_corpus(3, "更新的文本1", "更新的文本2")  # 更新ID为3的语料
