# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

"""
Sử dụng Python làm máy tính
    + Toán tử toán học
    + Toán tử gán
    + Toán tử so sánh
    + Toán tử boolean
    + Toán tử logical
    + Toán tử membership
    + Toán tử identity
    + Độ ưu tiên của toán tử
    + Các hàm toán học
"""


# Nhập đoạn chương trình sau và chạy chương trình để xem kết quả hiện ra
print(4000 + 1000 - 3000)
print(12 * 3 / 4)

""" Các toán tử toán học:
    Phép toán      Ý nghĩa          Ví dụ
        +           Cộng            2 + 3 = 5
        -           Trừ             1 - 10 = -9
        *           Nhân            5 * 8 = 40
        /           Chia            21 / 5 = 4.2
        //      Chia lấy nguyên     21 // 5 = 4
        %       Chia lấy dư         21 % 5 = 1
        **          Lũy thừa        2 ** 3 = 8 (2^3)
"""

# Nhập đoạn chương trình sau và rồi chạy để kiểm tra kết quả
print(2 + 3)
print(1 - 10)
print(5 * 8)
print(21 / 5)
print(21 // 5)
print(21 % 5)
print(2 ** 3)


""" Toán tử gán """
# Khai báo biến và gán giá trị phải thực hiện cùng lúc
x = 1
y = 2
print(x + y)

# Thực hiện gán các giá trị cho nhiều biến đồng thời
a, b, c = 1, 2, 3
tb = (a + b + c) / 3
print(tb)

# Gán cùng 1 giá trị cho nhiều biến
i = j = k = 0
print(i)
print(j)
print(k)

# Gán có tính update
a = 10  # giá trị gán lúc đầu
a = 2 * a + 6  # giá trị a sẽ được cập nhật mới = giá trị a cũ nhân 2 rồi cộng 6
print(a)
# Để cập nhật giá trị cho biến thì cần có gán giá trị ban đầu

""" Các cú pháp tắt cho việc cập nhật giá trị
        Cú pháp ngắn        Cú pháp đầy đủ
        n += 1              n = n + 1
        n -= 2              n = n - 2
        n *= 3              n = n * 3
        n /= x              n = n / x
        n **= 4             n = n ** 4
        a %= b              a = a % b
"""
# Tự viết chương trình check lại các cú pháp trên

""" Các Toán tử so sánh:
    Phép toán           Ý nghĩa
        ==              So sánh bằng. True nếu 2 bên bằng nhau
        !=              So sánh khác (không bằng). True nếu 2 bên khác nhau
        >               So sánh lớn hơn. True nếu bên trái lớn hơn bên phải
        >=              So sánh lớn hơn hoặc bằng. True nếu bên trái lớn hơn hoặc bằng bên phải
        <               So sánh nhỏ hơn. True nếu bên trái nhỏ hơn bên phải
        <=              So sánh nhỏ hơn hoặc bằng. True nếu bên trái nhỏ hơn hoặc bằng bên phải
"""

x = 3000
y = 5000
print('x == y is', x == y)
print('x != y is', x != y)
print('x > y is', x > y)
print('x < y is', x < y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)


""" 
- Các Toán tử logical:
    Phép toán           Ý nghĩa
    not x               Phủ định của x. True nếu x False và ngược lại
    x and y             Kiểm tra điều kiện đồng thời. True nếu cả x và y đều True, nếu không thì False
    x or y              Kiểm tra có 1 trong 2 điều kiện đúng. False nếu cả x và y đều False, nếu không thì True
    
- Bảng giá trị chân lý cho các phép toán:
    x           y           not x           x and y         x or y
    True        True        False           True            True
    True        False       False           False           True
    False       True        True            False           True
    False       False       True            False           False
"""

# Nhập chương trình sau và chạy thử để kiểm tra kết quả
a = True
b = False
print(a + 9)
print(b + 9)
print('not a is:', not a)
print('not b is:', not b)
print('a or b is:', a or b)
print('a and b is:', a and b)


""" Toán tử membership: 
    - in: True nếu giá trị hoặc biến có trong chuỗi
    - not in: True nếu giá trị hoặc biến không có trong chuỗi
"""

x = 'Halo Python '

print('H' in x)
print('hello' not in x)


""" Toán tử identity:
    - is: True nếu các vế giống hệt nhau (tham chiếu đến cùng một đối tượng)
    - is not: True nếu các vế không giống hệt nhau (tham chiếu đến khác đối tượng)
"""

x = 6
y = 5
a = 'Halo'
b = 'Halo'
i = [1, 2, 3]
j = [1, 2, 3]

print(x is not y)
print(a is b)
print(i is j)

""" Độ ưu tiên của toán tử 
    - Nguyên tắc PEMDAS: 
        P   Parentheses, then
        E   Exponents, then
        MD  Multiplication and division, left to right, then
        AS  Addition and subtraction, left to right
    - Chi tiết tại: https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

a = 10-7//2*3+1
# Lần lượt như sau: 7 // 2 = 3 ==> 10 - 3*3 + 1 ==> 3*3 = 9 ==> 10 - 9 + 1 = 2
print(a)

""" Các hàm toán học"""

# Người dùng nhập vào bán kình đường tròn, tính diện tích in ra màn hình
radius = float(input("Nhập bán kính = "))
area = 3.14 * radius ** 2
print("Hình tròn bán kính {} thì diện tích là {}".format(radius, area))


import math

radis = float(input("Nhập bán kính = "))
area = math.pi * radis ** 2
print("Hình tròn bán kình {} thì diện tích là {}".format(radis, round(area, 3)))

""" Một số hàm và hằng số trong module math
    - Hằng số: math.pi, math.e
    - Căn bậc 2: math.sqrt(x)
    - Làm tròn xuống: math.floor(x); Làm tròn lên: math.ceil(x); Bỏ phần thập phân: math.trunc(x)
    - Giai thừa: math.factorial(n)
    - Ước chung lớn nhất: math.gcd(a, b)
    - Lượng giác: math.sin(x), math.cos(x), math.tan(x), math.asin(x), .... 
"""

import math
print(math.pi)
print(math.e)
print(math.floor(0.9))
print(math.ceil(1.1))
print(math.trunc(-10.901))
print(math.factorial(3))
print(math.gcd(36, 63))
