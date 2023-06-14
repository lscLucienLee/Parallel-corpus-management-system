import os
import csv


class ParallelCorpusManager:
    def __init__(self):
        pass

    def create_corpus_csv(self, corpus_path):
        with open(corpus_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'original', 'translation']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print(f'平行语料库CSV文件已创建: {corpus_path}')

    def rename_corpus(self, corpus_path, new_corpus_name):
        new_corpus_path = os.path.join(os.path.dirname(corpus_path), new_corpus_name)
        os.rename(corpus_path, new_corpus_path)
        print(f'语料库已重命名为: {new_corpus_path}')

    def delete_corpus(self, corpus_path):
        os.remove(corpus_path)
        print(f'语料库已删除: {corpus_path}')

# # 使用示例
# manager = ParallelCorpusManager()

# # 创建一个平行语料库CSV文件
# manager.create_corpus_csv('corpus.csv')

# # 重命名语料库文件
# manager.rename_corpus('corpus.csv', 'new_corpus.csv')

# # 删除语料库文件
# manager.delete_corpus('new_corpus.csv')
