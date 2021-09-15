""" BÀI TẬP VỀ NHÀ

Bài 01. Ngân hàng Vietcombank sẽ cho khách hàng vay tiền nếu họ trên 18 tuổi và khoản thu nhập hằng năm tối thiểu 2500$.
Với biến chỉ tuổi của khách là age, biến chỉ thu nhập là income, hãy viết biểu thức logic để kiểm tra một khách hàng có được vay vốn hay không?

Bài 02. Code đoạn chương trình để giải quyết các yêu cầu sau:
    1. Nhập 3 số thực x, y, z bất kì.
    2. Tính giá trị biểu thức F: F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
    3. Đưa giá trị tính được của F ra màn hình dưới dạng: Gia tri cua F = <gia tri>

Bài 03. Hãy viết đoạn chương trình thực hiện các việc sau:
    1. Nhập hai số nguyên a và b từ bàn phím
    2. Thực hiện phép chia lấy nguyên (//) và chia lấy dư (%) của a cho b
    3. In kết quả 2 phép chia ra màn hình
    Lưu ý: Khi nhập giá trị để test, cần thực hiện các trường hợp sau và xem kết quả thu được
    - TH1: a > 0, b < 0
    - TH2: a < 0, b > 0
    - TH3: a < 0, b < 0
"""

# Bài 01.
age = int(input('Age = '))
income = int(input('Income = '))
print(age > 18 and income >= 2500)

# Bài 2.
import math

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
z = float(input("Nhập z: "))
F = (x + y + z)/(x**2 + y**2 + 1) - abs(x - z * math.cos(y))
print(f"Gia tri cua F = {F}")
