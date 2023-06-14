import csv

class CorpusRemover:
    def __init__(self, corpus_file_path):
        self.corpus_file_path = corpus_file_path

    def remove_duplicates(self):
        with open(self.corpus_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            # 获取 CSV 文件的列名
            header = next(reader)

            # 定义一个用于存储去重后的语料库数据的列表
            deduplicated_corpus = []

            # 定义一个用于存储已经出现过的语料库数据的集合
            seen_data = set()

            # 遍历 CSV 文件中的每一行数据
            for row in reader:
                # 将每一行数据转换为一个字典
                row_dict = {header[i]: row[i] for i in range(len(header))}

                # 如果该行数据还没有出现过，则保存它
                data_tuple = (row_dict['text1'], row_dict['text2'])
                if data_tuple not in seen_data:
                    seen_data.add(data_tuple)
                    deduplicated_corpus.append(row_dict)

        # 将去重后的语料库数据写回到 CSV 文件中
        with open(self.corpus_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            for row in deduplicated_corpus:
                writer.writerow(row)

        # 返回去重后的语料库数据
        return deduplicated_corpus

# if __name__ == '__main__':
#     corpus_handler = CorpusHandler('corpus.csv')
#     deduplicated_corpus = corpus_handler.remove_duplicates()

#     # 输出去重后的语料库数据
#     for data in deduplicated_corpus:
#         print(data)