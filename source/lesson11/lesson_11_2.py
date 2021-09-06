# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"


""" Class or Statíc Variable:
    - Được khai báo trong class nhưng bên ngoài các method
    - Được truy cập thông qua class chứ không cần object
    - Biến class/static là khác biệt và không conflict với các thuộc tính khác cùng tên
"""


class Pet:
    # class variable
    quantity = 0

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        Pet.quantity += quantity


dog = Pet('Dog', 5)
cat = Pet('Cat', 4)
python = Pet('Python', 2)

print(f"Dog: {dog.quantity}")
print(f"Cat: {cat.quantity}")
print(f"Python: {python.quantity}")

print(f"Total: {Pet.quantity}")
# Cách khác
print(f"{dog.__class__.quantity}")
print(f"{cat.__class__.quantity}")
print(f"{python.__class__.quantity}")


""" Minh hoạ cho việc thay đổi giá trị của class variable """


class Demo:
    class_var = 10


print(Demo.class_var)  # 10

# Truy cập qua object
obj_demo = Demo()
print(obj_demo.class_var)  # 10

# Thay đổi qua object
obj_demo.class_var = 100
print(obj_demo.class_var)  # 100
print(Demo.class_var)  # 10

# Thay đổi qua class
Demo.class_var = 50
print(obj_demo.class_var)  # 100
print(Demo.class_var)  # 50

# Đối với object, class_var là của nó và khi thay đổi qua object thì chỉ thay đổi class_var của object đó thôi
# Tương tự, khi mà thay đổi class_var qua class thì chỉ thay đổi class_var của class thôi
# => Do vậy, có thể hình dung, chúng ta có 2 biến khác nhau trong cùng class có cùng tên: một static và một ordinary (thông thường)


""" Static Method trong Python: có 2 cách để định nghĩa static methods trong class """

""" @staticmethod:
    - Với việc dùng decorated trên thì tạo ra static method, và chia sẻ namespace với class
    - Method này không yêu cầu tham số bắt buộc nào, còn đối với object method thì có self là bắt buộc
    - Truy cập được vào các biến tĩnh của lớp
"""


class ExampleStatic:
    name = 'ExampleStatic'

    @staticmethod
    def static_method():
        print(f'{ExampleStatic.name} static_method() called')


class ChildExampleStatic1(ExampleStatic):
    name = 'ChildExampleStatic1'


class ChildExampleStatic2(ExampleStatic):
    name = 'ChildExampleStatic2'

    @staticmethod
    def static_method():
        print(f'{ChildExampleStatic2.name} static_method() called')


ExampleStatic.static_method()  # ExampleStatic
ChildExampleStatic1.static_method()  # ExampleStatic
ChildExampleStatic2.static_method()  # ChildExampleStatic2


""" @classmethod:
    - Khác với @staticmethod, thì @classmethod nhận một tham số bắt buộc - cls mà nó được gọi
"""


class ExampleStatic:
    name = 'ExampleStatic'

    @classmethod
    def static_method(cls):
        print(f'{cls.name} static_method() called')


class ChildExampleStatic1(ExampleStatic):
    name = 'ChildExampleStatic1'


class ChildExampleStatic2(ExampleStatic):
    name = 'ChildExampleStatic2'

    @classmethod
    def static_method(cls):
        print(f'{cls.name} static_method() called')


ExampleStatic.static_method()  # ExampleStatic
ChildExampleStatic1.static_method()  # ChildExampleStatic1
ChildExampleStatic2.static_method()  # ChildExampleStatic2


""" Which one should you use?
    - Lựa chọn đầu, cho phép truy cập vào biến tĩnh trong cùng một lớp
    - Hướng tiếp cận 2, cho phép sửa đổi class variable của các lớp con mà không cần viết lại method khi dùng Kế Thừa
"""
