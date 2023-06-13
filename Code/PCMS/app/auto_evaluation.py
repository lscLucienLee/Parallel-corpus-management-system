import csv
from nltk.translate.bleu_score import sentence_bleu
from typing import List

class autoTranslationEvaluator:
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

    def evaluate_translation(self, machine_translation: str, reference_translation: str) -> float:
        machine_tokens = machine_translation.split()
        reference_tokens = reference_translation.split()
        bleu_score = sentence_bleu([reference_tokens], machine_tokens)
        return bleu_score

    def evaluate_translations(self) -> float:
        corpus = self.read_corpus()
        translations = self.read_machine_translations()
        scores = []
        for mt_row in translations:
            for corpus_row in corpus:
                if mt_row[0] == corpus_row[0]:  # 原文匹配
                    score = self.evaluate_translation(mt_row[1], corpus_row[1])
                    scores.append(score)
                    break

        # 计算平均分
        avg_score = sum(scores) / len(scores)
        return avg_score


# # 使用示例
# evaluator = autoTranslationEvaluator("corpus.csv", "machine_translations.csv")
# avg_score = evaluator.evaluate_translations()
# print(f"整个文件的平均得分: {avg_score}")
