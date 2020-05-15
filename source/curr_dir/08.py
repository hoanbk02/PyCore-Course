# # coding=utf-8
# __author__ = "hoanbk02@gmail.com"
# __copyright__ = "Copyright 2020, Phạm Phú Hoàn"
#
# """ File, Directory/Folder
#     - Open, Read, Write, Close File
#     - Various methods with file object
#     - Create, Rename, Listing Dir
# """
#
# """ File:
#     - Là nơi trên ổ cứng để lưu trữ các thông tin có liên quan đến nhau.
#     - Dạng lưu trữ vĩnh viễn (trong bộ nhớ dài hạn - ổ cứng, usb, ...) >< lưu trữ tạm thời (lưu dữ liệu cho chương trình đang thực thi) - RAM/Thanh ghi
#     RAM/Thanh ghi: ngắt điện thì mất dữ liệu >< dùng file là lưu đc mãi
#     - Để thao tác với file (tệp tin): Open => Thao tác (đọc, ghi) => Đóng lại (=> Áp dụng vào lập trình)
# """
#
# """ Open file:
#     - hàm open() => file object (đối tượng kiểu file)
#     - Định nghĩa đầy đủ hàm: open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# """
#
# f1 = open('file_test_open')  # Mở file nằm cùng thư mục với chương trình đang chạy
# f2 = open('/home/hoanpp/Desktop/PyCore-Course/PyCore-Course/source/curr_dir/file_test_open')
# # Mở file với đường dẫn tuyệt đối của file
# # Trên windown: C:/Python38/README.txt
#
# """ Các chế độ mở file (mode)
#     - r: read - Mở file để đọc (giá trị mặc định của mode)
#     - w: write - Mở file để ghi (tạo file mới nếu như file chưa tồn tại, hoặc nếu như file đã tồn tại thì ghi đề nội dung mới lên nội dung cũ)
#     - x: execute - Mở file để thực thi. Nếu như file ko tồn tại thì fail
#     - a: append - Mở file để ghi thêm vào cuối file (nếu file ko tồn tại thì tạo mới file)
#     - t: text - Mở ở chế độ văn bản (giá trị mặc đinh)
#     - b: binary - Mở ở chế độ nhị phân
#     - +: Mở file để cập nhật (đọc và viết)
# """
#
# f3 = open('file_test_open.txt')  # <=>  open('file_test_open.txt', 'r') hoặc open('file_test_open.txt', 'rt')
# f4 = open('file_test_open.txt', 'w')  # Ghi với dạng text
# f5 = open('file_test_open.txt', 'r+b')  # Đọc và ghi ở dạng nhị phân
#
# """ Chú ý, không giống như nhiều ngôn ngữ khác,
#     ký tự trong file ví dụ như a ko phải là 97 nếu như ko chỉ định sử dụng mã ASCII.
#     Hơn nữa, mỗi hệ điều hành lại chọn 1 kiểu mã hóa khác nhau, Win dùng cp1252, Linux thì dùng utf-8.
#     => Ko nên dùng mã hóa mặc định, vì trên mỗi hệ điều hành nó sẽ hoạt động khác nhau.
#     => Khi làm việc với file văn bản thì chúng ta nên chỉ rõ lại mã hóa sẽ dùng
# """
#
# f6 = open('file_test_open.txt', mode='r', encoding='utf-8')
#
# """ Đóng file:
#     - Khi hoàn thành các thao tác thì cần đóng file đúng cách
#     - Đóng file để giải phóng các tài nguyên gắn với file
#     - Hàm dùng close()
# """
#
# f7 = open('file_test_open.txt', encoding='utf-8')
# # Làm gì đó với file f7 ở trên
# f7.close()
#
#
# """ Nếu khi làm gì đó với file mà có lỗi thì sẽ ko thể đóng được file
#     - Cách 1: Dùng thêm try-finally (sẽ được học sau)
#     - Cách 2: Dùng với with - cách tốt nhất, không cần có close(), mặc định khi nào hết khối with thì file sẽ được đóng
# """
#
# with open('file_test_open.txt', encoding='utf-8') as f:
#     # Làm gì đó với file ở đây
#     pass
#
# """ Ghi dữ liệu vào file:
#     - Mở file ở chế độ w, a hoặc x
#     - Khi thao tác = w, thì lưu ý, nội dung cũ bị ghi dè => mất nội dung cũ
#     - hàm write() => trả về số ký tự đã đc ghi
# """
#
# with open("file_test.txt", 'w', encoding='utf-8') as f:
#     # f.write("00000\n")
#     # f.write("my first file\n")
#     # f.write("This file\n\n")
#     # f.write("contains three lines\n")
#     # f.write("4 line!")
#     f.write("Test ghi đè!")

""" Đọc file
    - Dùng chế độ r
    - hàm read(size), size dữ liệu mà chúng ta muốn đọc (tạm hiểu, là số ký tự)
    - Nếu như ko chỉ định size, thì nó đọc hết file
"""
#
# f_read = open('file_test.txt', 'r', encoding='utf-8')
# print(f_read.read(4))  # Đọc 4 ký tự đầu
# print(f_read.read(4))  # Đọc 4 ký tự tiếp theo 4 ký tự đầu
# print(f_read.read())  # Đọc tiếp đến khi nào hết dữ liệu
# print(f_read.read())  # Đọc tiếp => hết file rồi nên trả về chuỗi rỗng

""" Nguyên tắc hoạt động của read là dịch chuyển một con trỏ ảo đi lần lượt các dữ liệu trong file,
    sau mỗi lần read xong số lượng mong muốn thì con trỏ đó vẫn duy trì và đứng sẵn tại đó chờ câu lệnh read tiếp theo - nếu có
    Để thay đổi vị trí của của con trỏ thì dùng hàm seek()
    Hàm tell() trả lại vị trí hiện tại (tính theo đơn vị byte)
"""

# f_read = open('file_test.txt', 'r', encoding='utf-8')
#
# print(f_read.read())
# print(f_read.tell())  # Lấy vị trí hiện tại của con trỏ đọc file
# f_read.seek(5)  # Cho con trỏ về lại đầu file
# print(f_read.read(5))
# f_read.seek(5)
# print(f_read.read(5))

""" Làm thế nào để đọc từng dòng trong file => dùng vòng lặp for, hoặc readline() hoặc readlines() """

# f = open('file_test.txt', 'r', encoding='utf-8')

# for line in f:
#     print(line, end='')
# Chú ý, mặc định mỗi dòng đều đã có xuống dòng, để đỡ bị dòng trắng thì ta dùng end='' cho câu lệnh print

# print(f.readline())
# print(f.readline())
#
# print(f.readlines())  # Trả lại toàn bộ các dòng trong file dưới dạng list

""" Một số hàm hay dùng khác đối với file:
    - readable(): Trả lại True nếu luồng file có thể đọc
    - readline(n=-1): Đọc và trả lại một dòng từ file. Nếu n được chỉ định thì đọc tối đa n byte
    - readlines(n=-1): Đọc và trả về một danh sách các dòng từ file. Nếu n được chỉ định thì đọc tối đa n byte/ký tự
    - seek(offset, from=SEEK_SET): Thay đổi vị trí con trỏ file đến offset byte, tính từ from (Đầu, Hiện tại, Kết thúc)
    - seekable(): Trả lại True nếu luồng file có hỗ trợ truy cập ngẫu nhiên
    - truncate(size=None): Thay đổi size của luồng file thành size byte, nếu size ko được chỉ định, thì thay đến vị trí hiện tại
    - writable(): Trả lại True nếu luồng file cho phép ghi
    - writelines(lines): Ghi một list các dòng vào trong file
"""

""" Directory
    - Khi có nhiều file để xử lý trong chương trình Python, thì sắp xếp vào các thư mục để dễ quản lý
    - Một thư mục (directory/folder) là một tập hợp các file và thư mục con
    - Python cung cấp module os chứa nhiều phương thức để làm việc với directory (và cả file khá tốt)
"""

""" Cách lấy đường dẫn thư mục hiện tại, dùng getcwd() """

import os
print(os.getcwd())

""" Cách di chuyển sang thư mục khác dùng chdir() """
os.chdir('/home/hoanpp/Desktop/')
print(os.getcwd())

""" Cách lấy danh sách thu mục con và file dùng listdir() """

os.chdir('/home/hoanpp/Desktop/')
print(os.listdir())  # Lấy từ thư mục đang làm việc
print(os.listdir('/home/hoanpp/Desktop/PyCore-Course'))  # Lấy từ thư mục chỉ định

""" Tạo ra thư mục mới bằng: mkdir() """

os.mkdir('test_dir')
print(os.listdir())

""" Đổi tên thư mục hoặc file, dùng rename() """
print(os.listdir())
os.rename('test_dir', 'new_test_dir')
print(os.listdir())

""" Xóa bỏ thư mục hoặc file, dùng rmdir() - cái này chỉ dùng xóa đi được thư mục rỗng,
    còn dùng rmtree() trong module shutil để remove toàn bộ thư mục,
    còn file thì dùng remove()
"""
print(os.listdir())
os.remove('old.txt')
print(os.listdir())
os.rmdir('new_one')
print(os.listdir())

