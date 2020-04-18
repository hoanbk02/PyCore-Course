# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

"""
- Conditional Statements: if, if-else, nested if-else
- Loop: for, while, nested loops
- Control loop: break, continue, pass
"""

"""
- Kiểu dữ liệu boolean chỉ có 2 giá trị: True - Đúng, False - Sai
- Các phép toán trên kiểu dữ liệu boolean:
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


""" Các phép toán so sánh:
    Phép toán           Ý nghĩa
        ==              So sánh bằng. True nếu 2 bên bằng nhau
        !=              So sánh khác (không bằng). True nếu 2 bên khác nhau
        >               So sánh lớn hơn. True nếu bên trái lớn hơn bên phải
        >=              So sánh lớn hơn hoặc bằng. True nếu bên trái lớn hơn hoặc bằng bên phải
        <               So sánh nhỏ hơn. True nếu bên trái nhỏ hơn bên phải
        <=              So sánh nhỏ hơn hoặc bằng. True nếu bên trái nhỏ hơn hoặc bằng bên phải
"""
x = 2000
y = 3000
print('x == y is', x == y)
print('x != y is', x != y)
print('x > y is', x > y)
print('x < y is', x < y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

""" Câu lệnh rẽ nhánh. Khi trong bài toán xuất hiện việc điều khiển chương trình theo một số hướng nhất định,
nên đã xuất hiện câu lệnh điều kiện.
"""

# Ví dụ: Viết chương trình kiểm tra số nhập vào là số dương hay không.
# => Với các thứ đã học thì ko làm được ví dụ này
""" Cú pháp của if
    if biểu_thức_điều_kiện:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là đúng (True)
"""
n = float(input())
if n > 0:
    print('n = {} là số dương!'.format(n))
print('Đây là lệnh ngoài if, nó luôn luôn được in ra!')

# Ví dụ áp dụng: Nhập vào 1 số nguyên và in ra giá trị tuyệt đối của số đó
n = int(input())
if n < 0:
    n = -n
print(n)

""" Cú pháp của if-else
    if biểu_thức_điều_kiện:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là Đúng (True)
    else:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện là Sai (False)
"""

# Chương trinh kiểm tra số nhập vào là dương hay không dương
n = float(input())
if n > 0:
    print('n = {} là số dương!'.format(n))
else:
    print('n = {} là số không dương!'.format(n))

""" Cú pháp của if-elif-else
    if biểu_thức_điều_kiện_01:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_01 là Đúng (True)
    if biểu_thức_điều_kiện_02:
        các câu lệnh cần chạy nếu biểu_thức_điều_kiện_02 là Đúng (True)
    else:
        các câu lệnh cần chạy nếu các biểu_thức_điều_kiện ở trên đềy là Sai (False)
"""
n = float(input())
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
a = int(input())
b = int(input())
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
# Nhắc lại về phép toán gán với tính chất update
a = 10  # giá trị gán lúc đầu
a = 2 * a + 6  # giá trị a sẽ được cập nhật mới = giá trị a cũ nhân 2 rồi cộng 6
print(a)
# Để cập nhật giá trị cho biến thì cần có gán giá trị ban đầu

""" Các cú pháp tắt cho cho việc cập nhật giá trị
        Cú pháp ngắn        Cú pháp đầy đủ
        n += 1              n = n + 1
        n -= 2              n = n - 2
        n *= 3              n = n * 3
        n /= x              n = n / x
        n **= 4             n = n ** 4
        a %= b              a = a % b
"""
# Tự viết chương trình check lại các cú pháp trên

""" Cú pháp cho vòng for
    for i in sequence:
        các câu lệnh sẽ chạy của mỗi vòng lặp
"""
# Ví dụ: In ra cá giá trị nguyên từ 0 đến 9
for i in range(10):
    print(i)

""" Hàm range(start=0, stop, step_size=1): Generate a sequence of numbers
    + start: giá trị bắt đầu sinh.
    + stop: giá trị kết thúc sinh, có nghĩa là sinh đến giá trị bé hơn stop. Không có mặc định
    + step_size: bước nhảy để sinh các giá trị tiếp theo từ start (nhận cả giá trị âm và dương)
"""

# Ví dụ: In ra cá giá trị nguyên chẵn có một chữ số
for i in range(0, 10, 2):
    print(i, end=" ")

""" Hàm print(*args, sep=' ', end='\n', file=None):
    + *args: Cho phép in nhiều giá trị cùng lúc
    + sep: Kí tự dùng để phân tách các giá trị cần in. Mặc định là 1 khoảng trắng
    + end: Kí tự kết thúc sau khi in xong tất cả các giá trị. Mặc định là xuống dòng
"""

# Nhập vào 2 số nguyên a, b. In ra các số nguyên nằm giữa a và b trên cùng 1 dòng.

a, b = int(input()), int(input())
if a > b:
    a, b = b, a
for i in range(a, b + 1):
    print(i, end=" ")

# Ví dụ: Nhập vào số tự nhiên n, rồi tính giai thừa của n
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("{}! = {}".format(n, factorial))

# Ví dụ: Nhập vào số tự nhiên n, tính tổng các số chia hết cho 3 mà nhỏ hơn n
n = int(input())
sum_three = 0
for i in range(0, n, 3):
    sum_three += i
print("Tổng các số nhơ hon {} mà chia hết cho 3 la: {}".format(n, sum_three))

""" Nested for - Các lệnh for lồng nhau hay for trong for """

# Ví dụ: In ra màn hình hình một hình chữ nhật toán các ký tự @ kích thước n, m
n, m = int(input()), int(input())
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()


""" Cú pháp cho vòng while
    while biểu_thức_điều_kiện:
        các câu lệnh sẽ chạy của mỗi vòng while, một vòng while được chạy khi biểu_thức_điều_kiện là Đúng (True)
"""

# Nhập vào một số tự nhiên n rồi tính tổng các số tự nhiên đến n
n = int(input())
i = 0
sum_n = 0
while i <= n:
    sum_n = sum_n + i
    i += 1  # tăng biến đếm lên 1
print("Tổng các số tự nhiên đến {} là: {}".format(n, sum_n))
