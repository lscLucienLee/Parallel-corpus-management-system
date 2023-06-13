import csv
from typing import List, Dict

class TranslationComparison:
    def __init__(self, corpus_name: str, machine_translation_file: str):
        self.corpus_name = corpus_name
        self.machine_translation_file = machine_translation_file

    def read_corpus(self) -> List[List[str]]:
        corpus = []
        with open(self.corpus_name, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                corpus.append([row['original'], row['translation']])
        return corpus

    def read_machine_translations(self) -> List[List[str]]:
        translations = []
        with open(self.machine_translation_file, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # 跳过表头
            for row in reader:
                translations.append([row[0], row[1]])
        return translations

    def compare_translations(self) -> List[Dict[str, str]]:
        corpus = self.read_corpus()
        translations = self.read_machine_translations()
        comparison_data = []

        for mt_row in translations:
            for corpus_row in corpus:
                if mt_row[0] == corpus_row[0]:  # 原文匹配
                    comparison_data.append({
                        'original': mt_row[0],
                        'file1_translation': corpus_row[1],
                        'file2_translation': mt_row[1]
                    })
                    break

        return comparison_data


# # 使用示例
# comparer = TranslationComparison("corpus.csv", "machine_translations.csv")
# comparison_data = comparer.compare_translations()


