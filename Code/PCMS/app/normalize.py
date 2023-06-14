import csv
import unicodedata

class TextNormalizer:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data

    def write_csv(self, data):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'original', 'translation']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def normalize(self, text):
        normalized_text = unicodedata.normalize('NFKD', text)
        normalized_text = ''.join([c for c in normalized_text if (c >= '\u4e00' and c <= '\u9fa5') or (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c in [' ', ',', '.', '?', '!'])])
        return normalized_text

    def process_csv(self):
        data = self.read_csv()
        for row in data:
            row['original'] = self.normalize(row['original'])
            row['translation'] = self.normalize(row['translation'])
        self.write_csv(data)

# def main():
#     file_path = 'corpus.csv'  # 指定CSV文件路径
#     normalizer = TextNormalizer(file_path)
#     normalizer.process_csv()

# if __name__ == '__main__':
#     main()
