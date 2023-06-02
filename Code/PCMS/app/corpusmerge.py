import csv
import os

class CorpusMerger:
    def __init__(self):
        pass

    def merge_corpora(self, output_name, *corpora_paths):
        with open(output_name, 'w', newline='', encoding='utf-8') as output_file:
            fieldnames = ['id', 'original', 'translation']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            id_counter = 1
            for corpus_path in corpora_paths:
                with open(corpus_path, 'r', encoding='utf-8') as input_file:
                    reader = csv.DictReader(input_file)
                    for row in reader:
                        row['id'] = id_counter
                        writer.writerow(row)
                        id_counter += 1

        print(f'已合并{len(corpora_paths)}个语料库并保存为: {output_name}')

# # 使用示例
# merger = CorpusMerger()

# # 合并多个平行语料库CSV文件
# merger.merge_corpora('merged_corpus.csv', 'corpus1.csv', 'corpus2.csv', 'corpus3.csv')
