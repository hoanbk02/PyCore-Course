""" BÀI TẬP VỀ NHÀ

Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng

Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file

Bài 03: Viết chương trình trộn 2 file thành file mới

Bài 04: Viết hàm
        def get_file_size(file)
    để lấy và trả về dung lượng của file

Bài 05: Viết hàm
        def extract_characters(*file)
    trả lại tập các ký tự trong các file

Bài 06: Viết chương trình tạo ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
"""

# Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng

n = int(input("Bạn muốn đọc bao nhiêu dòng từ file file_test.txt? "))
with open('file_test.txt', 'r', encoding='utf-8') as f_read:
    for i in range(n):
        line = f_read.readline().rstrip("\n")
        print(f'Dòng {i+1}: {line}')


# Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file, thành 1 dòng mới

str = input('Bạn muốn thêm chuỗi gì vào cuối file file_test.txt? ')
with open('file_test.txt', 'a', encoding='utf-8') as f_append:
    f_append.write('\n' + str + '\n')


# Bài 03: Viết chương trình trộn 2 file thành file mới

with open('file_01.txt', 'r', encoding='utf-8') as fread:
    data_file1 = fread.read()

with open('file_02.txt', 'r', encoding='utf-8') as fread:
    data_file2 = fread.read()

with open('file_03.txt', 'w', encoding='utf-8') as fwrite:
    fwrite.write(data_file1 + data_file2)

# Bài 04: Viết hàm
#         def get_file_size(file)
#     để lấy và trả về dung lượng của file

import os


def get_file_size(file):
    return os.path.getsize(file)


file = 'file_test.txt'
print(f'File {file} có dung lượng: {get_file_size(file)} bytes')


# Bài 05: Viết hàm
#         def extract_characters(*files)
#     trả lại tập các ký tự trong các file

def extract_characters(*files):
    res = set()
    for file in files:
        with open(file, 'r', encoding='utf-8') as fread:
            res.update(set(fread.read()))
    return res


f1, f2, f3 = 'file_01.txt', 'file_02.txt', 'file_03.txt'
print(f'Các ký tự trong các file là: {extract_characters(f1, f2, f3)}')


# Bài 06: Viết chương trình tạo ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
import string

upper_char = string.ascii_uppercase
os.chdir('./temp_dir/')
for c in upper_char:
    os.mknod(f"{c}.txt")
