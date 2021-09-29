""" BÀI TẬP VỀ NHÀ

Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
    Sau đó, unpack các phần tử trong một tuple.

Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple

Bài 02: Viết chương trình đảo ngược một tuple.

Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.

Bài 04: Cho 1 list chứa các tuple không rỗng.
    Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]

Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.

Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.

Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.

Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.

Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.

Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.

Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.

Bài 12. Viết chương trình để thử lại các phương thức của Set theo danh sách sau
        set.difference_update(other_set)
        set.intersection_update(other_set)
        set.isdisjoint(other_set)
        set.issubset(other_set)
        set.issuperset(other_set)
        set.symmetric_difference_update(other_set)

"""

# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.

demo_tuple = (1, 3.14, 2+3j, 'tuple', [0, 1, True], False, )
a, b, c, d, e, f = demo_tuple
print(demo_tuple)
print(a, b, c, d, e, f)


# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
tuple_2_list = list((0, 1, 2, 3, 5, 6, 3, 8, 9))
print(tuple_2_list)
list_2_tuple = tuple([0, 1, 5, 6, 2, 7, 9, 2, 0, 6])
print(list_2_tuple)


# Bài 02: Viết chương trình đảo ngược một tuple.
tuple_sample = (0, 1, 2, 3, 4, 5, 6)
reverse_tuple = tuple_sample[::-1]
print(reverse_tuple)


# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
list_demo = [0, 0.2, 'string', 5, [3, 2, 1], (0, ), [4, 7, 'temp']]
count = 0
for item in list_demo:
    if type(item) == tuple:
        break
    else:
        count += 1
print(f'Có {count} phần tử trong list trước khi gặp tuple')


# Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#     Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
list_sample = [(2, 5), (4, 1), (0, 0)]
for i in range(len(list_sample)):
    for j in range(i+1, len(list_sample)):
        if list_sample[i][-1] > list_sample[j][-1]:
            list_sample[i], list_sample[j] = list_sample[j], list_sample[i]
print(list_sample)


# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple
list_demo = [(0, 1), (3, 2, 0), (0, -1), (4, 5), (9, 2), (4, 1)]
minn = list_demo[0][1]
item_min = list_demo[0]
for item in list_demo:
    if item[1] < minn:
        minn = item[1]
        item_min = item
print(f'Tuple có phần tử thứ 2 là nhỏ nhất {item_min}')


# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
tuple_demo = (0, 2, 4, 6, [1, 2, 0], ['str', 'chuoi', 'string'], 3.14, 7, -3, 't')
print(f'Phần tử thứ 4: {tuple_demo[3]}')
print(f'Phần tử thứ 4 từ cuối lên: {tuple_demo[-4]}')


# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
tuple_1 = (0, 3, 5, 7, 9, 10)
tuple_2 = (4, 5, 9, 10, 12, -4)
flag = False
for item in tuple_1:
    if item in tuple_2:
        flag = True
print(f"2 tuple có phần tử chung hay không? {flag}")


# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
tuple_the_same = (0, 0.0, 0**1, 0*9, 0/2)
if tuple_the_same.count(tuple_the_same[0]) == len(tuple_the_same):
    print("Tất cả các phần tử trong tuple CÓ giống nhau")
else:
    print('Tất cả các phần tử trong tuple KHÔNG giống nhau')


# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
tuple_float = (0.1, -2.17, 200/11, 3.3, 5/6, -4/7, 11.01)
maxx = tuple_float[0]
tong = 0
for item in tuple_float:
    tong += item
    if item > maxx:
        maxx = item
print(f'Tổng là {tong}, GTLN là {maxx}')


# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
list_domain = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
list_hauto = []
for item in list_domain:
    list_hauto.append(item.split('.')[-1])  # Xem chi tiết về hàm split trong bài học về String. Ở đây tách theo dấu chấm
print(f'Danh sách hậu tố của tên miền {tuple(list_hauto)}')


# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
str_input = input('Nhập câu văn: ')
list_word = str_input.strip().split(' ')  # Tách theo khoảng trắng để ra được các từ đơn
maxx = list_word[0]
for item in list_word:
    if len(item.strip()) > len(maxx):
        maxx = item.strip()
print(f'Từ dài nhất trong câu: {maxx}')

