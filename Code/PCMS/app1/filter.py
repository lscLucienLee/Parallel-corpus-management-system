import csv
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

class Corpusfilter:
    def __init__(self, corpus_file_path):
        self.corpus_file_path = corpus_file_path
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def filter_corpus(self):
        with open(self.corpus_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)

            # 获取 CSV 文件的列名
            header = next(reader)

            # 定义一个用于存储过滤后的语料库数据的列表
            filtered_corpus = []

            # 遍历 CSV 文件中的每一行数据
            for row in reader:
                # 将每一行数据转换为一个字典
                row_dict = {header[i]: row[i] for i in range(len(header))}

                # 在这里对每一行数据进行过滤
                text1 = row_dict['text1']
                text2 = row_dict['text2']
                text1_filtered = self._filter_text(text1)
                text2_filtered = self._filter_text(text2)

                # 保存过滤后的语料库数据
                filtered_corpus.append({
                    'id': row_dict['id'],
                    'text1': text1_filtered,
                    'text2': text2_filtered
                })

        # 返回过滤后的语料库数据
        return filtered_corpus

    def _filter_text(self, text):
        # 去除 HTML 标记
        text = re.sub('<[^<]+?>', '', text)

        # 句子/段落分割
        sentences = sent_tokenize(text)

        # 定义一个用于存储过滤后的文本的列表
        filtered_text = []

        # 遍历每一个句子/段落
        for sentence in sentences:
            # 去除标点符号、数字等非文本内容
            sentence = re.sub(r'[^\w\s]', '', sentence)
            sentence = re.sub(r'\d+', '', sentence)

            # 分词
            words = word_tokenize(sentence)

            # 去除停用词和低频词，进行词干提取
            words_filtered = []
            for word in words:
                if word.lower() not in self.stopwords:
                    word_lemmatized = self.lemmatizer.lemmatize(word.lower(), pos='v')
                    if len(word_lemmatized) > 2:
                        words_filtered.append(word_lemmatized)

            # 将过滤后的词语重新组成句子/段落
            sentence_filtered = ' '.join(words_filtered)
            if sentence_filtered:
                filtered_text.append(sentence_filtered)

        # 将过滤后的文本重新组成一个字符串
        filtered_text = ' '.join(filtered_text)

        return filtered_text