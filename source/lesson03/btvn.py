""" BÀI TẬP VỀ NHÀ

Bài 1. Code đoạn chương trình cho phép:
    1. Nhập vào bán kình r của hình tròn
    2. Tính diện tích hình tròn đó
    3. In kết quả ra màn hình "Dien tich hình tron la: <giá trị>"

Bài 2. Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>

Bài 3. Xây dựng đoạn chương trình mô phỏng lại các phép toán học (càng nhiều càng tốt),
tối thiểu cần có: cộng, trừ, nhân, chia

"""

# Bài 1.
r = float(input("Nhập bán kinh hình tròn: "))
s = 3.14 * r**2
print(f'Dien tich hình tron la: {s}')

# Bài 2.
import math

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
z = float(input("Nhập z: "))
F = (x + y + z)/(x**2 + y**2 + 1) - abs(x - z * math.cos(y))
print(f"Gia tri cua F = {F}")
