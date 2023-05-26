import csv
from nltk.translate.bleu_score import sentence_bleu
from typing import List

class autoTranslationEvaluator:
    def __init__(self, corpus_name: str):
        self.corpus_name = corpus_name

    def read_corpus(self) -> List[List[str]]:
        corpus = []
        with open(self.corpus_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                corpus.append(row)
        return corpus

    def evaluate_translation(self, machine_translation: str, reference_translation: str) -> float:
        machine_tokens = machine_translation.split()
        reference_tokens = reference_translation.split()
        bleu_score = sentence_bleu([reference_tokens], machine_tokens)
        return bleu_score

    def evaluate_translations(self, translations: List[str]) -> List[float]:
        corpus = self.read_corpus()
        scores = []
        for mt, ref in zip(translations, corpus):
            scores.append(self.evaluate_translation(mt, ref[2]))
        return scores


# # 使用示例
# evaluator = autoTranslationEvaluator("corpus.csv")
# translations = ["机器翻译结果1", "机器翻译结果2", "机器翻译结果3"]
# scores = evaluator.evaluate_translations(translations)

# for i, score in enumerate(scores):
#     print(f"翻译 {i+1} 的BLEU分数: {score}")
