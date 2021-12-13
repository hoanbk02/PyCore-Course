""" BÀI TẬP VỀ NHÀ

Bài 00. Viết chương trình tính tích value của các phần tử trong một dict

Bài 01. Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất trong các value của dict

Bài 02. Viết chương trình tìm ra top 3 phần tử của dict có key lớn nhất

Bài 03. Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict

Bài 04. Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict

Bài 05. Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}

Bài 06. Viết chương trình lấy ra top 3 phần tử có value lớn nhất từ dict

Bài 07. Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}

Bài 08: Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản

Bài 09: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}
"""

# Bài 00. Viết chương trình tính tích value của các phần tử trong một dict

dict_00 = {
    0: 1,
    2: 3,
    'k': 4,
    'x': 5,
    -1: 2
}
tich_value = 1
for item in dict_00:
    tich_value *= dict_00[item]
print(f"Tích các value trong dict: {tich_value}")
# Hoặc dùng cách sau
tich_value = 1
for key, value in dict_00.items():
    tich_value *= value
print(f"Tích các value trong dict: {tich_value}")

# Bài 01. Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất trong các value của dict
from math import inf
dict_01 = {
    -2: 9,
    0: 1,
    2: 3,
    'k': 4,
    'x': 5,
    -1: 2,
    3: -3
}
maxx = -inf
minn = inf
for k, v in dict_01.items():
    if v < minn:
        minn = v
    if v > maxx:
        maxx = v
print(f'Value max = {maxx}, min = {minn}')

# Bài 02. Viết chương trình tìm ra top 3 phần tử của dict có key lớn nhất
dict_03 = {
    -2: 9,
    4: -1,
    2: 3,
    -1: 2,
    3: -3,
    6: 4,
    -9: 5,
    0: 9,
    -8: 3
}
keys_sorted = sorted(dict_03.keys(), reverse=True)
result = [(keys_sorted[0], dict_03[keys_sorted[0]]), (keys_sorted[1], dict_03[keys_sorted[1]]), (keys_sorted[2], dict_03[keys_sorted[2]])]
print(f" phần tử có key lớn nhất {result}")

# Bài 03. Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
dict_04 = {
    'key1': [0, 2, 4, 1, 3, 5, 6],
    'key2': [0, -2, 4, 1, -3, 5, 0],
    'key3': [-2, 4, 1, -3, -5, 0],
    'key4': [0, -2, -4, 1, -3, 5],
    'key5': [0, 4.314, 1, -3, 5, 0.1],
}
for k, v in dict_04.items():
    print(f'Phần tử thứ 5 của value trong phần tử với key = {k} là: {v[4]}')

# Bài 04. Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
dict_051 = {
    1: 1,
    2: 2,
    3: 3,
    4: 5,
    6: 7
}
dict_052 = {
    1: -1,
    2: -2,
    -3: 3,
    4: 5,
    6: -7
}
result = set()
for k, v in dict_051.items():
    if k in dict_052 and v == dict_052[k]:
        result.add((k, v))
print(f"Các phần tử key-value xuất hiện trong cả 2 dict: {result}")

# Bài 05. Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}
sample = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = {k: sample[k] for k in keys}
print(f'Kết quả của bài toán {result}')

# Bài 06. Viết chương trình lấy ra top 3 phần tử có value lớn nhất từ dict
dict_07 = {
    -2: 9,
    4: -1,
    2: 3,
    -1: 2,
    3: -3,
    6: 4,
    -9: 5,
    0: 9,
    -8: 3
}
values_max_sorted = sorted(dict_07.values(), reverse=True)[0:3]
result = set()
for k, v in dict_07.items():
    if v in values_max_sorted:
        result.add((k, v))
print(f'Kết quả của bài toán {result}')

# Bài 07: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
input_str = 'Stringings'
set_char = set(input_str)
result = {}
for c in set_char:
    result[c] = input_str.count(c)
print(f'Kết quả bài toán {result}')

# Bài 08: Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
from string import punctuation
import re

input_09 = '''Mot cau van trong doan van. Day la vi du ve sinh doan van de tach tu don.'''
r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
set_word = r.split(input_09)
result = {}
for w in set_word:
    result[w] = set_word.count(w)
print(f'Kết quả của bài toán: {result}')

# Bài 09: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output = {}
for ele in input:
    name = ele['item']
    amount = ele['amount']
    if name in output:
        output[name] += amount
    else:
        output[name] = amount
print(f'Kết quả: {output}')
