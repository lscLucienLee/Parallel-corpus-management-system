import csv

class CorpusSplitter:
    def __init__(self):
        pass

    def split_corpus(self, corpus_path, *split_infos):
        # 读取原始语料库
        with open(corpus_path, 'r', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            rows = list(reader)

        # 计算拆分点
        total_ratio = sum(info['ratio'] for info in split_infos)
        split_points = [int(len(rows) * info['ratio'] / total_ratio) for info in split_infos[:-1]] + [len(rows)]

        # 拆分语料库并保存新文件
        start = 0
        for i, split_info in enumerate(split_infos):
            end = min(start + split_points[i], len(rows))
            with open(split_info['output_name'], 'w', newline='', encoding='utf-8') as output_file:
                fieldnames = ['id', 'original', 'translation']
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()

                for j, row in enumerate(rows[start:end], start=1):
                    row['id'] = j
                    writer.writerow(row)

            start = end
            print(f'已根据占比拆分语料库并保存为: {split_info["output_name"]}')


# # 使用示例
# splitter = CorpusSplitter()

# # 拆分平行语料库CSV文件
# split_infos = [
#     {'ratio': 3, 'output_name': 'split_corpus1.csv'},
#     {'ratio': 4, 'output_name': 'split_corpus2.csv'},
# ]

# splitter.split_corpus('corpus.csv', *split_infos)
