import csv
import re
from collections import Counter


class CorpusAnalyzer:
    def __init__(self, corpus_file_path):
        self.corpus_file_path = corpus_file_path

    def read_corpus(self):
        with open(self.corpus_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            content = [row for row in reader]
        return content

    def word_counter(self, text):
        words = re.findall(r'\w+', text.lower())
        return Counter(words)

    def analyze_corpus(self):
        content = self.read_corpus()
        total_counter = Counter()
        for row in content[1:]:
            total_counter += self.word_counter(row[1])
            total_counter += self.word_counter(row[2])

        top_five_words = total_counter.most_common(5)
        total_sentences = len(content) - 1

        return {
            "top_five_words": top_five_words,
            "total_sentences": total_sentences
        }

    def search_word_frequency(self, word):
        content = self.read_corpus()
        word = word.lower()
        total_counter = Counter()
        for row in content[1:]:
            total_counter += self.word_counter(row[1])
            total_counter += self.word_counter(row[2])

        word_frequency = total_counter.get(word, 0)
        return word_frequency

    def save_results_to_csv(self, results):
        with open(self.corpus_file_path, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['top_five_words', 'total_sentences']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(results)

# def main():
#     corpus_file_path = 'corpus.csv'
#     corpus_analyzer = CorpusAnalyzer(corpus_file_path)
#     results = corpus_analyzer.analyze_corpus()
#     corpus_analyzer.save_results_to_csv(results)

# if __name__ == '__main__':
#     main()
