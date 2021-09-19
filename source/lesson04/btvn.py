""" BÀI TẬP VỀ NHÀ

Bài 01. Lập chương trình thực hiện công việc sau:
    1. Nhập ba số a, b, c bất kì từ bàn phím
    2. Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0  (Xét tất cả các trường hợp có thể xảy ra)

Bài 02. Lập chương trình tính các tổng sau:
    S_1 = 1 + x + x^2 + x^3 + ... + x^n
    S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
    S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
    Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím

Bài 03. Lập chương trình thực hiện các công việc sau:
    1. Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    2. Tính tổng các chữ số của số đó.
    3. Hiển thị kết qủa ra màn hình

Bài 04. Lập trình thực hiện các công việc sau:
    1. Nhập 3 số a, b, c bất kì
    2. Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
    3. Nếu đúng là tam giác thì xác định là tam giác vuông hay không?

Bài 05. Lập chương trình thực hiện các công việc sau:
    1. Nhập số epsilon < 1 từ bàn phím
    2. Tính e = 1 + 1/1! + 1/2! + ... + 1/n! quá trình dừng khi 1/n! < epsilon.
    3. Đưa kết quả ra màn hình
"""

# Bài 1.
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có nghiệm: x_0 = {-c/b}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm thực")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép x_0 = {-b/(2*a)}")
    else:
        sqrt_delta = math.sqrt(delta)
        print(f"Phương trình có 2 nghiệm: x_1 = {(-b + sqrt_delta)/(2*a)}, x_2 = {(-b - sqrt_delta)/(2*a)}")


# Bài 2
x = float(input("Nhập x: "))
n = int(input("Nhập n:"))
S1 = 0
for i in range(n+1):
    S1 += x ** i
print(f"Giá trị S1 = {S1}")


x = float(input("Nhập x: "))
n = int(input("Nhập n:"))
S2 = 0
for i in range(n+1):
    S2 += (-x) ** i
print(f"Giá trị S2 = {S2}")


x = float(input("Nhập x: "))
n = int(input("Nhập n:"))
S3 = 0
for i in range(n+1):
    S3 += x ** i / math.factorial(i)
print(f"Giá trị S3 = {S3}")


# Bài 3.
while True:
    n = int(input("Nhập giá trị n dương (< 1000): "))
    if 0 < n < 1000:
        break
    print("Nhập chưa đúng, hãy nhập lại!")

tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(f"Tổng các chữ số của {n} là {tong}")


# Bài 4.
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Là độ dài 3 cạnh của tam giác.")
    if a == b and b == c:
        print("Tam giác đều")
    elif a == b or b == c or c == a:
        print("Tam giác cân")
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        print("Tam giác vuông")
else:
    print("Không phải độ dài 3 cạnh của tam giác.")


# Bài 5.
epsilon = float(input("Nhập epsilon = "))
fact_max = 1/epsilon  # Đổi lại điều kiện dừng lặp
i = 1
factorial = 1
value_e = 1
while factorial <= fact_max:
    value_e += 1 / factorial
    i += 1
    factorial *= i
print(f'Giá trị của e ~ {value_e}')