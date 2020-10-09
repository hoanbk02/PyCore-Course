""" OOPs trong Python
    - Python cho phép lập trình đa mô hình.
    - Phổ biến là hướng đối tượng - Object oriented programming
    - Một đối tượng thì đặc trưng bởi: Thuộc tính (attributes) và Hành vi (behavior)
    - Xét ví dụ:
        Cat là đối tượng có:
            - tên, tuổi, màu lông => Thuộc tính
            - kêu, chạy, ăn, uống => Hành vi
    - OOP trong python tập trung vào tái sử dụng code, DRY - Dont repeat yourself
    - Trong Python, OOP có một số nguyên tắc sau:
        - Inheritance - Kế thừa: Sử dụng các chi tiết từ 1 class mới mà ko làm thay đổi gì class đã có
        - Encapsulation - Đóng gói: Ẩn đi các chi tiết riêng của một class đối với các object hay class khác
        - Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào khác nhau
"""

""" Class - Bản phác thảo cho object"""
""" Attribute - Thuộc tính"""
""" Method - Là các định nghĩa hàm bên trong class, dùng để định nghĩa hành vi của object"""

class Cat:
    # class attribute - thuộc tính của class
    loai = "Thú họ Mèo"

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # instance method
    def run(self):
        return f"{self.name} đang chạy"

    def eat(self, food):
        return f"{self.name} thích ăn {food}"


# # instance of Cat class - Khai báo 2 đối tượng của lớp Cat
# mun = Cat("Mun", 1, "Đen")
# vang = Cat("Vàng", 2, "Vàng")
#
# # Truy cập class attr
# print(f"Mun là {mun.__class__.loai}")
# print(f"Vàng là {vang.__class__.loai}")
#
# # Truy vấn đến instance attr
# print(f"{mun.name} đã {mun.age} tuổi và lông màu {mun.color}")
# print(f"{vang.name} đã {vang.age} tuổi và lông màu {vang.color}")

# cam = Cat("Cam", 3, "Vàng, Trắng")
# print(cam.run())
# print(cam.eat("cá"))


""" Inheritance - Kế thừa
    - Là cách tạo ra class mới có sử dụng chi tiết từ class đã có mà ko thay đổi nó
    - Lớp mới được gọi là lớp dẫn xuất (hoặc lớp con), lớp đã có là lớp cơ sở (hoặc lớp cha)
"""

# Ví dụ:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Tạo Person!')

    def who_am_i(self):
        print('Person')

    def speak(self, lang='Tiếng Việt'):
        print(f'{self.name} nói {lang}')


class StudentIT(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        print('Tạo StudentIT!')

    def who_am_i(self):
        print('StudentIT')

    def code(self, lang):
        print(f'{self.name} lập trình {lang}')


# svbk = StudentIT("Peter", 20, "HUST")
# svbk.who_am_i()
# svbk.speak()
# svbk.code("Python")


""" Encapsulation - Đóng gói
    - Trong Python, có thể hạn chế quyền truy cập vào các phương thức và biến => ngăn dữ liệu ko bị sửa đổi trực tiếp
    => được gọi là Đóng gói - Encapsulation
    - Dùng ký hiệu cho thuộc tính private là 2 gạch dưới __
"""

# Ví dụ
# class Laptop:
#
#     def __init__(self):
#         self.__price = 500
#
#     def sell(self):
#         print(f'Giá bán là {self.__price}')
#
#     def set_price(self, price):  # setter
#         self.__price = price


# lap = Laptop()
# lap.sell()
#
# # thay đổi giá trị price, cố tình truy cập vào thuộc tính
# lap.__price = 1000
# lap.sell()
#
# # thay đổi qua hàm setter
# lap.set_price(1000)
# lap.sell()


""" Polymorphism - Đa hình
    - Là khả năng (trong OOP) cho phép dùng chung interface cho nhiều hình thái (kiểu dữ liệu)
    - Ví dụ cho dễ hiểu: Cần tô màu cho một hình, có nhiều hình: vuông, tròn, chữ nhật, ...; nhưng có thể dùng cùng một
    phương thức để tô màu cho hình => Đây chính là đa hình
"""
class PC:
    def wifi(self):
        print('Không kết nối được!')


class Laptop:
    def wifi(self):
        print('Kết nối được rồi!')


def connect_wifi(computer):
    computer.wifi()


lap = Laptop()
pc = PC()

connect_wifi(lap)
connect_wifi(pc)


""" Lưu ý:
    - Lập trình trở lên dễ dàng và hiệu quả
    - Class có thể chia sẻ, nên code có thể sử dụng lại
    - Năng suất của chương trình tăng
    - Dữ liệu được an toàn và bảo mật với sự trừu tượng hóa dữ liệu
"""

class Employee:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.luong = 0


class NVVP(Employee):

    def tinh_luong(self, ngay_lam):
        self.luong = ngay_lam * 100000


class NVSX(Employee):

    def tinh_luong(self, luong_cb, san_pham):
        self.luong = luong_cb + san_pham * 5000



