import csv
import subprocess
from typing import List, Dict

class FastAlignWrapper:
    def __init__(self, corpus_name: str, fast_align_path: str):
        self.corpus_name = corpus_name
        self.fast_align_path = fast_align_path

    def convert_to_fast_align_format(self, input_csv, output_txt):
        with open(input_csv, 'r', encoding='utf-8') as csvfile, open(output_txt, 'w', encoding='utf-8') as txtfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                txtfile.write(f"{row['original']}\t{row['translation']}\n")

    def run_fast_align(self, input_txt, output_txt):
        forward_align = f"{self.fast_align_path} -i {input_txt} -d -o -v > {output_txt}"
        subprocess.run(forward_align, shell=True)

    def parse_fast_align_output(self, input_txt):
        aligned_data = []

        with open(input_txt, 'r', encoding='utf-8') as txtfile:
            for line in txtfile:
                original, translation, alignment_str = line.strip().split(' ||| ')
                original_words = original.split()
                translation_words = translation.split()
                alignments = alignment_str.split()

                aligned_original_words = []
                aligned_translation_words = []

                for alignment in alignments:
                    orig_idx, trans_idx = map(int, alignment.split('-'))
                    aligned_original_words.append(original_words[orig_idx])
                    aligned_translation_words.append(translation_words[trans_idx])

                aligned_data.append({
                    'num': len(aligned_original_words),
                    'original': aligned_original_words,
                    'translation': aligned_translation_words
                })

        return aligned_data

    def align_words(self) -> List[Dict[str, List[str]]]:
        input_csv = self.corpus_name
        input_txt = 'fast_align_corpus.txt'
        output_txt = 'aligned_words.txt'

        self.convert_to_fast_align_format(input_csv, input_txt)
        self.run_fast_align(input_txt, output_txt)
        aligned_data = self.parse_fast_align_output(output_txt)

        return aligned_data

# # 使用示例
# fast_align_path = 'path/to/fast_align/build/fast_align.exe'  # 替换 fast_align.exe 路径
# corpus_name = 'corpus.csv'
# aligner = FastAlignWrapper(corpus_name, fast_align_path)
# aligned_data = aligner.align_words()

# for data in aligned_data:
#     print(data)
# 克隆 fast_align 仓库并构建可执行文件：

# 打开一个命令提示符窗口，并进入到您希望存放 fast_align 代码的目录。
# 运行以下命令以克隆仓库： git clone https://github.com/clab/fast_align.git
# 进入 fast_align 目录： cd fast_align
# 创建构建目录： mkdir build && cd build
# 运行： cmake .. -DCMAKE_BUILD_TYPE=Release
# 构建可执行文件： cmake --build . --config Release
