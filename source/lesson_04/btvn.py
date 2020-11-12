""" BÀI TẬP VỀ NHÀ BUỔI 04 - List:

Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.

Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.

Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.

Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.

Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.

Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.

Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau

Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.

Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.

Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).

Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm
Example:
    Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
    => Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5]
"""

# Bài 08:
A = [9, 8, 7, 6, 5, 4, 3]
count = 0
for j in range(1, len(A)):
    for i in range(j):
        if A[i] > A[j]:
            count += 1
print(count)

# Bài 09:
mx_1 = [[1, 2, 3],
        [4, 5, 6],
        [1, 0, 0]]
mx_2 = [[2, 1, 0],
        [9, 0, 5],
        [0, 3, 7]]

result = []
row = len(mx_1)
col = len(mx_1[0])

for i in range(row):
    row_result = []
    for j in range(col):
        cell = 0
        for k in range(3):
            cell += mx_1[i][k] * mx_2[k][j]
        row_result.append(cell)
    result.append(row_result)

print(result)

# Bài 10:
A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]

# Cách 1:
result_1 = []
count_1 = 0
for item in A:
    if item not in result_1:
        count_1 += 1
        result_1.append(item)
print(count)


# Cách 2:
result_2 = set(A)
count_2 = len(result_2)