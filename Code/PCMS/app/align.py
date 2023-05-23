import csv
import os
from typing import List
from fast_align import align
from io import StringIO

class CorpusAligner:
    def __init__(self, corpus_name: str):
        self.corpus_name = corpus_name

    def read_corpus(self) -> List[List[str]]:
        corpus = []
        with open(self.corpus_name, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                corpus.append(row)
        return corpus

    def display_sentence_alignment(self, sentence_pairs: List[List[str]]):
        for i, (src, tgt) in enumerate(sentence_pairs):
            print(f"{i+1}. Source: {src}")
            print(f"   Target: {tgt}")

    def align_sentences(self, sentence_pairs: List[List[str]]) -> List[List[str]]:
        input_data = "\n".join(f"{src} ||| {tgt}" for src, tgt in sentence_pairs)
        aligned_output = align(StringIO(input_data))
        
        aligned_pairs = []
        for output_line in aligned_output.split('\n'):
            if not output_line.strip():
                continue
            src, tgt = output_line.split("|||")
            aligned_pairs.append(([s.strip() for s in src.split()], [t.strip() for t in tgt.split()]))
        return aligned_pairs

    def manual_alignment(self, aligned_pairs: List[List[str]]):
        for i, (src, tgt) in enumerate(aligned_pairs):
            while True:
                self.display_sentence_alignment([(src, tgt)])
                user_input = input(f"请在对齐不准确的地方进行修改，然后按回车键。输入'next'以进入下一句。")
                if user_input.lower() == 'next':
                    break

    def align_corpus(self):
        corpus = self.read_corpus()
        sentence_pairs = [(row[1], row[2]) for row in corpus]
        aligned_pairs = self.align_sentences(sentence_pairs)
        self.manual_alignment(aligned_pairs)


# # 使用示例
# aligner = CorpusAligner("corpus.csv")
# aligner.align_corpus()
