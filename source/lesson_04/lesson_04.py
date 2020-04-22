# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

# """ List
#     - Introduction
#     - Accessing list
#     - Operations
#     - Working with lists
#     - Functions and Methods
# """
#
# """ Introduction
#     - Python cung cấp cho chúng ta một loạt các kiểu dữ liệu hỗn hợp kiểu là một chuỗi liên tiếp gì đó.
#     - Trong đó, kiểu dữ liệu List - rất linh hoạt và được dùng thường xuyên nhất.
# """
#
# # Cách tạo ra một list: Đặt các phần tử vào trong cặp ngoặc vuông và cách nhau bởi dấu phẩy (,)
# empty_list = []  # Một list rỗng = list không có phần tử nào
# my_list = [26, 10, 1992, 28, -2000]  # Một list chứa các số nguyên
# your_list = [1, 'hi', 'greeting', 3.14]  # Một list hỗn hợp các kiểu dữ liệu
# our_list = ['123-string', [0, 1], ['str1', 'str-2'], [empty_list, my_list, your_list]]  # Nested list
#
# """ Truy cập vào list (=> Giống với chuỗi. Ta có thể coi chuỗi là 1 list, mỗi phần tử là một ký tự)
#     - Bằng chỉ số dương: Truy cập bằng chỉ số với toán tử []. Chỉ số được đánh từ 0, đến (Số lượng phần tử - 1).
#      Cố tính truy cập vào một gia trị chỉ số khác sẽ báo lỗi IndexError
#     - Bằng chỉ số âm: Chỉ số âm được đánh như sau: -1 là phần tử cuối cùng, ..., đến -(số lượng phần tử) là phần tử đầu tiên
#     - Bằng đoạn cắt: Sử dụng toán tử cắt dấu hai chấm
# """
# my_list = ["first", 1, 2, 3, 'l', [4, 5, 6, 7]]
# print(len(my_list))  # Hàm len() trả lại số lượng phần tử trong list
# print(my_list[0])
# print(my_list[3])
# print(my_list[5])
#
# # print(my_list[10])  # Lỗi IndexError: list index out of range
#
# # Trong trường hợp trên là có list lồng nhau
# print(my_list[5][2])  # Truy cập đến list con bằng [5], sau đó truy cập vào phần tử của list con bằng [3]
# print(my_list[0][1])  # Truy cập vào phần tử đầu tiên của my_list => được 1 chuỗi, rồi truy cập vào phần tử thứ 2 của chuỗi
#
# print(my_list[-2])  # Truy cập phần tử thứ 2 từ cuối lên
# print(my_list[-1][-1])  # Truy cập vào phần tử cuối cùng trong phần tử cuối cùng của my_list
# print(my_list[0][-3])  # Truy cập vào phần tử thứ 3 từ cuối lên trong phần tử đầu tiên của my_list
#
# print(my_list[2:5])
# print(my_list[:-3])
# print(my_list[3:])
# print(my_list[::3])
# print(my_list[::-1])
#
""" Các phép toán với kiểu dữ liệu list. Khác với chuỗi thì list là kiểu có thể thay đổi được.
    - Dùng phép gán (=) để thay đổi 1 phần tử tại chỉ số nào đó của list
    - 
"""
