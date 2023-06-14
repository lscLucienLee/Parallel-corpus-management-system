import csv

class TxtToCsvConverter:
    def __init__(self, input_txt_file, output_csv_file):
        self.input_txt_file = input_txt_file
        self.output_csv_file = output_csv_file

    def read_txt_file(self):
        with open(self.input_txt_file, 'r', encoding='utf-8') as file:
            data = [line.strip().split(',', 1) for line in file.readlines()]
        return data

    def write_csv_file(self, data):
        with open(self.output_csv_file, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'original', 'translation']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for index, row in enumerate(data, start=1):
                writer.writerow({'id': index, 'original': row[0], 'translation': row[1]})

    def convert(self):
        data = self.read_txt_file()
        self.write_csv_file(data)

# # 使用方法：
# # 创建TxtToCsvConverter类的实例，并提供输入的TXT文件路径和输出的CSV文件路径
# converter = TxtToCsvConverter('your_input_txt_file_path.txt', 'your_output_csv_file_path.csv')
# # 调用 convert 方法以将TXT文件转换为CSV文件
# converter.convert()
