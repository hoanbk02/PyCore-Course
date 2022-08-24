# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"


""" Chú thích trong Python
    Câu lệnh Output/Input
    Biến (Variable). Định danh, quy ước đặt tên
    Các kiểu dữ liệu:
        + Kiểu dữ liệu dựng sẵn: bool, sequences, sets, characters, literals
        + Kiểu dữ liệu người dùng định nghĩa
        + Hằng số
        + Xác định kiểu dữ liệu của biến
"""

""" Các cách viết comment
    + Comment 1 dòng dùng #
    + Comment nhiều dòng thì dùng # tại mỗi đầu dòng; hoặc dùng cặp 3 nháy đơn hoặc dùng cặp 3 nháy kép
"""
# Đoạn chương trình khai báo biến lưu trữ tên
# Và sau đó in ra lời chào mừng với tên đó
name = 'Phạm Hoàn'  # Một biến với tên name để lưu trữ tên của ai đó, phục vụ cho câu lệnh dưới
print('Chào mừng %s đến với thế giới Python.' % name)  # Câu lệnh in ra lời chào với biến name khai báo bên trên

"""
- Câu lệnh output => in gì đó ra màn hình console => print
- Câu lệnh input => nhận gì đó được nhập vào từ bàn phím => input
    + Gặp lệnh này, chương trình sẽ chờ người dùng nhập vào gì đó và bấm phím Enter
    + Lưu lại giá trị nhập này có thể dùng biến
    + Luôn nhận vào thành 1 chuỗi. Cần thì ép kiểu như phần trước - học sau
"""
name = input("Nhập tên ai đó: ")
print("Xin chào bạn %s nhé." % name)

# Nhập đoạn chương trình sau và chạy chương trình để xem kết quả hiện ra
print(4000 + 1000 - 3000)
print(12 * 3 / 4)


""" 
- Biến - Variable: Một cái tên/nhãn dùng để gọi một giá trị nào đó
- Dùng biến giúp chương trình mạch lạc, dễ hiểu
- Để gán giá trị vào biến ta dùng dấu bằng(=). Ví dụ: year_born = 1980, name = 'Py'
"""

# Nhập đoạn chương trình sau và chạy để kiểm tra kết quả
name = 'Python'
print(name + ' was born in')
year_born = 1980
print(year_born)


""" 
Quy tắc đặt tên biến:
    - Chỉ gồm chữ cái (a-z, A-Z) hoặc chữ số (0-9) hoặc gạch dưới (_)
    - Không bắt đầu bằng chữ số
    - Không được trùng với từ khóa của ngôn ngữ (bảng từ khóa)
    - Độ dài tùy ý
Ví dụ:
    - Hợp lệ: myClass, var_1, query_set, _products, ...
    - Không hợp lệ: 1_connection, global, class, text!, bien-1, ...
Lưu ý: 
    - Python là ngôn ngữ có phân biệt hoa và thường.
    - Đặt tên biến sao cho có tính gợi nhớ
    - Tên biến gồm nhiều từ thì cách nhau bằng gạch dưới
"""

# Sử dụng biến để làm bài sau: Tính trung bình cộng của 3 số đó
a = 1
b = 2
c = 3
tb = (a + b + c) / 3
print(tb)


""" Các kiểu dữ liệu dựng sẵn:
    + bool
    + Number: int, float, complex
    + characters, string
    + sequence, set, ...
"""

""" Kiểu dữ liệu người dùng định nghĩa """

# Nhập chương trình sau và chạy để xem kết quả.
var = 1992
print(var)
var = 10.26
print(var)
var = 2 + 1j
print(var)

b = True
print(b)
str = 'a string'
print(str)
cars = [1, 2, 4, 6, 3]
print(cars)

# var = 1990  # => int
# print(var)
# var = 10.25  # => float
# print(var)
# var = 1+3j  # => complex
# print(var)
# b = True  # => bool
# print(b)
# _str = 'a string'  # => string
# print(_str)
# cars = [1, 2, 3, 5, 7, 0]  # => list
# print(cars)

""" - Kiểu dữ liệu boolean chỉ có 2 giá trị: True - Đúng, False - Sai """

"""
- Xâu/Chuỗi ký tự là đoạn chữ, trong đó, mỗi thành phần nhỏ gọi là ký tự. 
- Thường đặt trong cặp dấu nháy kép hoặc dấu nháy đơn.
- Để khai báo chuỗi có nhiều dòng thì đặt đoạn chữ trong cặp 3 dấu nháy kép hoặc 3 dấu nháy đơn
"""

msg = '''Hồn tôi là một vườn hoa lá
Rất đậm hương và rộn tiếng chim...
- Trích Từ ấy của Tố Hữu - 
'''
print(msg)


""" Hằng số - Là biến mà không thể thay đổi giá trị sau khi đã khai báo.
Nhưng trong Python không có định nghĩa để khái báo về hằng số nhưng chúng ta có thể quy định với nhau,
khi tên biến được đặt tất cả bằng chữ in hoa thì nó ám chỉ 1 hằng số"""

PI = 3.1414
GRAVITY = 9.8
E = 2.718281828  # Hằng số Nê-pe (Napier)
print(PI)
print(GRAVITY)
print(E)


""" Xác định kiểu dữ liệu của biến. Kiểu dữ liệu của biến phụ thuộc vào giá trị mà nó đang lưu trữ
    + type(var): Cho biết kiểu dữ liệu của biến
    + isinstance(var, type): Trả lại đúng nếu var mang kiểu type và sai nếu không mang
"""

# Nhập chương trình sau và chạy để xem kết quả.
var = 1992
print(var, 'is of type', type(var))
var = 10.26
print(var, 'is of type', type(var))
var = 2 + 1j
print(var, 'is complex number?', isinstance(var, complex))
var = [1, 2, 3, 0, 6]
print(var, 'is of type', type(var))


# Nhúng giá trị vào trong chuỗi
name, py = 'Python', "Java"
print('Hello %s. I am %s' % (name, py))

x, y = 123, 987
print("Gia tri cua x la {}, y la {} và trung binh la: {}".format(x, y, (x+y)/2))

print("I love {0} and {1}".format('Python', 'JavaScript'))
print("I love {1} and {0}".format('Python', 'JavaScript'))
print("Hello {f_name}. I am {my_name}.".format(f_name='John', my_name='PyCore'))

# Nhúng cả biến, biểu thức vào trong chuỗi
print(f'{x} + {y} = {x+y}')

