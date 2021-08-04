# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

""" Câu lệnh điều khiển 
    - Conditional Statements: if, if-else, nested if-else
    - Loop: for, while, nested loops
    - Control loop: break, continue, pass, return
"""

""" Câu lệnh rẽ nhánh
    Khi trong bài toán xuất hiện việc điều khiển chương trình theo một số hướng nhất định,
    nên đã xuất hiện câu lệnh điều kiện.
"""

# Ví dụ: Viết chương trình kiểm tra số nhập vào là số dương hay không.
# => Với các thứ đã học thì ko làm được ví dụ này

""" 
Cú pháp của if

    if biểu_thức_điều_kiện:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là đúng (True)

"""

n = float(input("Nhập n = "))
if n > 0:
    print('n = {} là số dương!'.format(n))
print('Đây là lệnh ngoài if, nó luôn luôn được in ra!')

# Ví dụ áp dụng: Nhập vào 1 số nguyên và in ra giá trị tuyệt đối của số đó
n = int(input("Nhập n = "))
if n < 0:
    n = -n
print(n)


""" Cú pháp của if-else
    if biểu_thức_điều_kiện:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là Đúng (True)
    else:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là Sai (False)
"""

# Chương trình kiểm tra số nhập vào là dương hay không dương
n = float(input("Nhập n = "))
if n > 0:
    print('n = {} là số dương!'.format(n))
else:
    print('n = {} là số không dương!'.format(n))


""" Cú pháp của if-elif-else
    if biểu_thức_điều_kiện_01:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_01 là Đúng (True)
    elif biểu_thức_điều_kiện_02:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_02 là Đúng (True)
    else:
        các câu lệnh cần chạy nếu các biểu_thức_điều_kiện ở trên đềy là Sai (False)
"""
n = float(input("Nhập n = "))
if n == 0:
    print('n là số 0')
elif n > 0:
    print('n = {} là số dương!'.format(n))
else:
    print('n = {} là số âm!'.format(n))


""" Chương trình: Nhập vào 2 số nguyên, in ra màn hình:
    + Tổng của 2 số đó, nếu cả 2 số đều dương
    + Tích của 2 số đó nếu cả 2 số đều âm
    + Nếu không in ra màn hình số nhỏ hơn trong 2 số đó
"""
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))
if a > 0 and b > 0:
    print('Tổng = ', a + b)
elif a < 0 and b < 0:
    print('Tích = ', a * b)
else:
    if a < b:
        print(a)
    else:
        print(b)
# Cách khác cho else: print(a) if a < b else print(b) hoặc print(a if a < b else b)


"""
- Các chương trình máy tính thường sẽ thực hiện lặp đi lặp lại một số câu lệnh nào đó => gọi là vòng lặp
- Python có 2 dạng vòng lặp for và while
"""

""" 
Cú pháp cho vòng for

    for i in sequence:
        các câu lệnh sẽ chạy của mỗi vòng lặp

"""

# Ví dụ: In ra cá giá trị nguyên từ 0 đến 9
for i in range(10):
    print(i)

""" Hàm range(start=0, stop, step_size=1): Generate a sequence of numbers
    + start: giá trị bắt đầu sinh, mặc định = 0
    + stop: giá trị kết thúc sinh, có nghĩa là sinh đến giá trị bé hơn stop. Không có mặc định
    + step_size: bước nhảy để sinh các giá trị tiếp theo từ start (nhận cả giá trị âm và dương), mặc định = 1
"""

# range(10)  => range(0, 10, 1)
# range(0, 10, 2)  => 0, 2, 4, 6, 8
# range(1, 10, 2) => 1, 3, 5, 7, 9
# range(0, -10, -2) => 0, -2, -4, -6, -8
# range(-10, 0, 2) => -10, -8, -6, -4, -2


# Ví dụ: In ra cá giá trị nguyên chẵn có một chữ số
for i in range(0, 10, 2):
    print(i, end=" ")

""" Hàm print(*args, sep=' ', end='\n', file=None):
    + *args: Cho phép in nhiều giá trị cùng lúc
    + sep: Kí tự dùng để phân tách các giá trị cần in. Mặc định là 1 khoảng trắng
    + end: Kí tự kết thúc sau khi in xong tất cả các giá trị. Mặc định là xuống dòng
"""

# Nhập vào 2 số nguyên a, b. In ra các số nguyên nằm giữa a và b trên cùng 1 dòng.

a, b = int(input("Nhập a = ")), int(input("Nhập b = "))
if a > b:
    a, b = b, a
for i in range(a+1, b):
    print(i, end=" ")

# Ví dụ: Nhập vào số tự nhiên n, rồi tính giai thừa của n
n = int(input("Nhập n = "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Ví dụ: Nhập vào số tự nhiên n, tính tổng các số chia hết cho 3 mà nhỏ hơn n
n = int(input("Nhập n = "))
sum_three = 0
for i in range(0, n, 3):
    sum_three += i
print("Tổng các số nhỏ hơn {} mà chia hết cho 3 là: {}".format(n, sum_three))

""" Nested for - Các lệnh for lồng nhau hay for trong for """

# Ví dụ: In ra màn hình hình một hình chữ nhật toán các ký tự * kích thước n, m
n, m = int(input("Nhập n = ")), int(input("Nhập m = "))
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()


""" 
Cú pháp cho vòng while

    while biểu_thức_điều_kiện:
        các câu lệnh sẽ chạy của mỗi vòng while, một vòng while được chạy khi biểu_thức_điều_kiện là Đúng (True)

"""

# Nhập vào một số tự nhiên n rồi tính tổng các số tự nhiên đến n
n = int(input("Nhập n = "))
i = 0
sum_n = 0
while i <= n:
    sum_n = sum_n + i
    i += 1  # tăng biến đếm lên 1
print(f"Tổng các số tự nhiên đến {n} là: {sum_n}")

# Nhập vào một số tự nhiên x, tìm số n lớn nhất mà tổng các số tự nhiên đến n không vượt quá x
x = int(input("Nhập x = "))
n = 0
sum_n = 0
while sum_n <= x:
    n += 1
    sum_n = sum_n + n

print(f"Số n lớn nhất là {n-1}")

""" Lập chương trình thực hiện các công việc sau:
    + Nhập số epsilon < 1  từ bàn phím
    + Tính e = 1+\dfrac{1}{1!} + \dfrac{1}{2!} + ... +\dfrac{1}{n!} quá trình dừng khi \dfrac{1}{n!} <  epsilon.
    + Đưa kết quả ra màn hình
"""
epsilon = float(input("Nhập epsilon = "))
fact_max = 1/epsilon  # Đổi lại điều kiện dừng lặp
i = 1
factorial = 1
value_e = 1
while factorial <= fact_max:
    value_e += 1 / factorial
    i += 1
    factorial *= i
print('Giá trị của e ~ ', value_e)

""" Nested while và Nested for-while: Giống như phần Nested for """
outer = 1
while outer < 2:
    inner = 3
    while inner < 6:
        print(outer, ':', inner)
        inner += 1
    outer += 1


""" 
    Thay đổi luồng của vòng lặp. Các câu lệnh trong vòng lặp sẽ chạy mãi cho đến khi biểu_thức_điều_kiện Sai(False).
    Trong nhiều trường hợp, cần dừng vòng lặp hiện tại hoặc dừng hoàn toàn vòng lặp.
"""

""" Cú pháp của break - dừng toàn bộ việc lặp
        for val in sequence:
            ...
            if điều_kiện:
                break
            ...
        ...

        while biểu_thức_điều_kiện_w:
            ...
            if điều_kiện:
                break
            ...
        ...
"""
# Viết chương trình kiểm tra số mà người dùng nhập vào là số dương thì dừng lại

while True:
    print("Nhập 1 số nguyên:", end=" ")
    n = int(input())
    if n > 0:
        print("Đã nhập số dương. Chương trình đã dừng lại!")
        break
    print("Đã nhập số âm. Chương trình sẽ tiếp tục!")

""" Cú pháp của continue - dừng vòng lặp hiện tại
        for val in sequence:
            ...
            if điều_kiện:
                continue
            ...
        ...

        while biểu_thức_điều_kiện_w:
            ...
            if điều_kiện:
                continue
            ...
        ...
"""

# Chương trình chỉ in ra các số có 2 chữ số và ko chia hết cho 1 trong các số 2, 3, 5
for i in range(10, 100):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=" ")


""" pass
    - Là 1 câu lệnh rỗng
    - Trình thông dịch có thông dịch qua nó nhưng sẽ ko có chuyện gì xảy ra. Khác với comment, trình thông dịch bỏ qua
    - Dùng trong khi mà chúng ta chưa nghĩ ra phần thân cho các câu lệnh if, else, for, while, ...
"""

for i in range(10):
    pass


_str = 'example-pass'
if 'a' in _str:
    pass

""" return => sẽ giới thiệu trong phần học về function """
