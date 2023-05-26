import csv
from typing import List

class ManualEvaluation:
    def __init__(self, corpus_name: str):
        self.corpus_name = corpus_name

    def read_corpus(self) -> List[List[str]]:
        corpus = []
        with open(self.corpus_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                corpus.append(row)
        return corpus

    def display_translations(self, translations: List[str]):
        corpus = self.read_corpus()
        for i, (mt, ref) in enumerate(zip(translations, corpus)):
            print(f"{i+1}. Machine translation: {mt}")
            print(f"   Reference translations: {ref[1]}, {ref[2]}")

    def get_user_scores(scores: List[int]) -> List[int]:
        validated_scores = []
        for i, score in enumerate(scores):
            while True:
                try:
                    if 0 <= score <= 100:
                        validated_scores.append(score)
                        break
                    else:
                        print(f"分数应在0-100之间，翻译 {i+1} 的分数无效。")
                        break
                except ValueError:
                    print("请输入一个整数。")
        return validated_scores

    def calculate_average_score(self, scores: List[int]) -> float:
        return sum(scores) / len(scores)

    def evaluate_translations(self, translations: List[str],scores:List[int]):
        self.display_translations(translations)
        score = self.get_user_scores(scores)
        average_score = self.calculate_average_score(score)
        return average_score


# # 使用示例
# evaluator = ManualEvaluation("corpus.csv")
# translations = ["机器翻译结果1", "机器翻译结果2", "机器翻译结果3"]
# evaluator.evaluate_translations(translations)
