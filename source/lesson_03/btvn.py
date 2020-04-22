""" BÀI TẬP VỀ NHÀ BUỔI 03 - String

Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.

Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.

Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.

Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.

Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.

Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.

"""


# Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
s_01 = input("Nhập vào một chuỗi: ")
if len(s_01) > 0:
    print(s_01.replace(s_01[0], '$'))
print('Bài 01 - DONE!')


# Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
s_02 = input("Nhập vào một chuỗi: ")
if s_02:
    m = int(input("Vị trí muốn xóa: "))
    if 0 <= m < len(s_02):
        s_new = s_02[:m] + s_02[m+1:]
        print("Chuỗi mới: " + s_new)
    else:
        print('Không thể tìm được vị trí cần xóa!')
print('Bài 02 - DONE!')


# Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
s_03 = input("Nhập vào một chuỗi: ")
s_new = s_03[0::2]
print("Chuỗi mới: " + s_new)
print('Bài 03 - DONE!')


# Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
# nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
s_04 = input("Nhập vào một chuỗi: ")
s_new = ""
if len(s_04) >= 2:
    s_new = s_04[0:2] + s_04[-2:]
print("Chuỗi mới: " + s_new)
print('Bài 04 - DONE!')


# Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
s_05 = input("Nhập vào một chuỗi: ")
if s_05:
    c_max, c_min = s_05[0], s_05[0]
    for c in s_05:
        if c > c_max:
            c_max = c
        elif c < c_min:
            c_min = c
    print(f"Ký tự lớn nhất {c_max} và nhỏ nhất {c_min}")
print('Bài 05 - DONE!')


# Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
s_06 = input("Nhập vào một chuỗi: ")
s_new = ""
for c in s_06:
    if 'a' <= c <= 'z':
        s_new = s_new + chr(ord(c) - 32)
    elif 'A' <= c <= 'Z':
        s_new = s_new + chr(ord(c) + 32)
    else:
        s_new = s_new + c
print("Chuỗi mới: " + s_new)
print('Bài 06 - DONE!')
