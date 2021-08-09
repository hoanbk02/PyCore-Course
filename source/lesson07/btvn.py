""" BÀI TẬP VỀ NHÀ

Bài 00. Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.

Bài 01. Viết chương trình tính tổng, tích của các phần tử trong một list.

Bài 02. Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.

Bài 03. Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.

Bài 04. Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.

Bài 05. Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.

Bài 06. Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau

Bài 07. Viết chương trình kiểm tra 2 list có phần tử chung hay không.

Bài 08. Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.

Bài 09. Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).

Bài 10.
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
"""


# Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
import random

list_goc = [0, 1, 2, 'boy', 1-2j, 5, 8, 9, 4, 'a']
random.shuffle(list_goc)  # Sẽ trộn ngẫu nhiên các phần tử trong list_goc => tạo ra đc thứ tự ngẫu nhiên
list_moi = list_goc[:5]  # Lấy ra 5 phần tử đầu => đc list chứa 5 phần tử ngẫu nhiên
print(list_moi)


# Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.
alist = [-4, 9, 3, 4, 5, -8, 2, 1, -6, 3]
tong = 0
tich = 1
for item in alist:
    tong += item
    tich *= item

print(f"Tổng = {tong}, tích = {tich}")
# Hoàn toàn có thể tính tổng bằng hàm sum() cung cấp sẵn trong Python


# Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
one_list = [1, 0, 9, 4, 5, 2, 7, 8, 3]
maxx = one_list[0]
minn = one_list[0]
for item in one_list:
    if maxx < item:
        maxx = item
    elif minn > item:
        minn = item

print(f'Max = {maxx}, min = {minn}')
# Hoàn toàn có thể dùng hàm được cung cấp sẵn max(), min() để tim GTLN, GTNN


# Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
the_list = ['girl', 'mot', 'hai', 'Hai', 'Huy', 'Cuong', 'PythonCore']
s = input("Nhập chuỗi s: ")

# Cách 1:
new_list = []
for item in the_list:
    new_list.append(s+item)
print(f'List mới: {new_list}')

# Cách 2:
new_list = [s+item for item in the_list]
print(f'List mới: {new_list}')


# Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
list_04 = [0, 2, 3, 7, 8, 5, 4, 6, 9, 0, 1]
l = int(input("Nhập độ dài phần đầu: "))
head = list_04[:l]
tail = list_04[l:]
print(f"Phần đầu: {head}, Phần sau: {tail}")


# Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
#         Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
list_05 = [0, 2, 3, 4, 5, 8, 9, 6, 7, 4, 3, 1, 3, 4, 2, 8, 0, 1, 5, 6]
most_item = 0
most_count = 0
for item in list_05:
    count_item = list_05.count(item)
    if most_count < count_item:
        most_count = count_item
        most_item = item
print(f"Giá trị: {most_item} xuất hiện {most_count}")


# Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
list_06 = ['most', 'anh', 'Viet', 'hoanh', 'b', 'ba', 'a', 'bcd', 'effe', 'nan', 'two', 'xxx', 'xyx']
count = 0
for item in list_06:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1
print(f"Có {count} thỏa mãn")


# Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
list_071 = ['b', 'ba', 'a', 'bcd', 'effe', 0, 3.0, 6, 1.7, 8, 4.13]
list_072 = ['xb', 2, 3.3, 'b5a', 4.13, 'a9', 'bd', 'effect', 1.7, 8]
chung = False
for item in list_071:
    if item in list_072:
        chung = True
        break
print(f"Hai list có phần tử chung không? {chung}")


# Bài 08: Cho list các số nguyên dương A.
#         Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
A = [1, 3, 6, 8, 4, 9, 0, 4, 5, 6, 2, 4, 7, 9, 4, 2]
n = len(A)
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            count += 1
print(f"Có {count} cặp số thỏa mãn")


# Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
matrix_A = [[-2, 3, 1],
            [-4, 0, 3],
            [2, -3, 4]]
matrix_B = [[1, 2, -3],
            [2, 3, 1],
            [3, 2, -2]]
matrix_C = []
m = len(matrix_A)
n = len(matrix_A[0])
p = len(matrix_B[0])

for i in range(m):
    temp = []
    for j in range(p):
        c_ij = 0
        for k in range(n):
            c_ij += matrix_A[i][k] * matrix_B[k][j]
        temp.append(c_ij)
    matrix_C.append(temp)

print(f"Kết quả: {matrix_C}")


# Bài 10:
# Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
#        Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
# Input: A - mảng chứa id của mỗi bài hát
# Output: Độ dài cần tìm
# Example:
#     Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
#     => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]

A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
temp = []
for item in A:
    if item not in temp:
        temp.append(item)
print(f"Chuỗi dài nhất là {len(temp)} các bài hát liên tiếp")
