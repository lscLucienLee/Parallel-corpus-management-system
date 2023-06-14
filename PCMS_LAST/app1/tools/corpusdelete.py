import csv
import os


class DeleteCorpus:
    def __init__(self, filename):
        self.filename = filename

    def delete_corpus(self, delete_id):
        updated_corpus = []
        with open(self.filename, 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if int(row["id"]) < int(delete_id):
                    updated_corpus.append(
                        {"id": row["id"], "original": row["original"], "translation": row["translation"]})
                elif int(row["id"]) > int(delete_id):
                    updated_corpus.append(
                        {"id": str(int(row["id"]) - 1), "original": row["original"], "translation": row["translation"]})

        with open(self.filename, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ["id", "original", "translation"]
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(updated_corpus)

# # 示例用法
# corpus = DeleteCorpus("your_corpus_filename.csv")
# corpus.delete_corpus(3)  # 删除ID为3的语料
