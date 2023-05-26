import csv
import re
from collections import Counter

class CorpusAnalyzer:
    def __init__(self, corpus_name):
        self.corpus_name = corpus_name

    def read_corpus(self):
        with open(self.corpus_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            content = [row for row in reader]
        return content

    def word_counter(self, text):
        words = re.findall(r'\w+', text.lower())
        return Counter(words)

    def analyze_corpus(self):
        content = self.read_corpus()
        total_counter = Counter()
        for row in content:
            total_counter += self.word_counter(row[1])
            total_counter += self.word_counter(row[2])

        top_five_words = total_counter.most_common(5)
        total_parallel_sentences = len(content)

        return {
            "top_five_words": top_five_words,
            "total_parallel_sentences": total_parallel_sentences
        }

    def search_word_frequency(self, word):
        content = self.read_corpus()
        word = word.lower()
        total_counter = Counter()
        for row in content:
            total_counter += self.word_counter(row[1])
            total_counter += self.word_counter(row[2])

        word_frequency = total_counter.get(word, 0)
        return word_frequency

# if __name__ == "__main__":
#     corpus_name = "your_corpus.csv"
#     analyzer = CorpusAnalyzer(corpus_name)

#     # 分析语料库
#     analysis_result = analyzer.analyze_corpus()
#     print(analysis_result)

#     # 搜索单词频率
#     search_word = "your_search_word"
#     word_frequency = analyzer.search_word_frequency(search_word)
#     print(f"The frequency of the word '{search_word}' is: {word_frequency}")
