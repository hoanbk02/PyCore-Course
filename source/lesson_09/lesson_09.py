# # coding=utf-8
# __author__ = "hoanbk02@gmail.com"
# __copyright__ = "Copyright 2020, Phạm Phú Hoàn"
#
# """ OOPs trong Python
#     - Python là một trong những ngôn ngữ lập trình đa mô hình => Python sẽ hỗ trợ nhiều phương pháp lập trình khác nhau
#     - Một trong những phương pháp tiếp cận phổ biến hiện nay là Hướng đối tượng - Object-Oriented Programming (OOP)
#     - Một đối tượng có hai đặc trưng:
#         - Thuộc tính (attributes)
#         - Hành vi (behavior)
#     - Xét ví dụ sau:
#         Cat là một đối tượng có:
#         - tên, tuổi, màu lông => Thuộc tính
#         - kêu, chạy, nhảy, ăn, uống => Hành vi
#     - Khái niệm OOP trong Python còn tập trung vào việc viết code có thể tải sử dụng, được biết đến như là DRY - Dont Repeat Yourself
#     - Trong Python, OOP theo một số nguyên tắc cơ bản như sau:
#         - Inheritance - Kế thừa: Sử dụng các chi tiết từ một class mới mà ko làm thay đổi gì class đã có
#         - Encapsulation - Đóng gói: Ẩn các chi tiết riêng tư của một class đối với các object khác
#         - Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào khác nhau
# """
#
# """ Class - Là bản thiết kế cho object
#     - Có thể hình dùng class như một bản phác thảo của một cat với các nhãn. Nó chứa tất cả chi tiết về name, age, ...
#     - Dựa trên các mô tả đó, chúng ta sẽ đi tìm hiểu về cat, ở đây, cat là một object
# """
# class Cat:
#     pass
# # Sử dụng keyword class để định nghĩa một class Cat - rỗng. Từ class, chúng ta sẽ khởi tạo được instance.
# # Một instance là một đối tượng riêng biệt từ lớp cụ thể
#
#
# """ Object
#     - Một object (instance) là một khởi tạo của một lớp
#     - Khi class được định nghĩa, thì chỉ có các mô tả của object được xác định
#     => không có bộ nhớ hoặc lưu trữ nào được phân bổ
# """
# obj_cat = Cat()
# # Ở đây, obj_cat là object của class Cat

# Chúng ta đã nói chi tiết về Mèo - Cat rồi, giờ sẽ cũng nhau đi xây dựng chi tiết về class và về object của Cat như sau:
class Cat:
    # class attribute - thuộc tính của class
    loai = 'Thú họ Mèo'

    # instance attribute - thuộc tính của đối tượng
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


# instance of Cat class - Khai báo 2 đối tượng của class Cat
muop = Cat('Mướp', 2, 'Vàng')
mun = Cat('Mun', 1, 'Đen')

# Truy cập class attribute
print(f'Mướp là', muop.__class__.loai)
print(f'Mun cũng là', mun.__class__.loai)

# Truy cập instance attribute
print(f'{muop.name} đã {muop.age} tuổi và lông màu {muop.color}')
print(f'{mun.name} đã {mun.age} tuổi và lông màu {mun.color}')

# Trong đoạn chương trình trên, đã tạo ra một class Cat với các attribute và các attribute là những đặc trưng của một object



