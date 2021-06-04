""" BÀI TẬP VỀ NHÀ:

Bài 00. Viết một chương trình để lấy ra tên class của một object?

Bài 01: Xem code đã có trong file btvn_01_dog.py.
    Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Tạo ra 3 đối tượng Dog với các thuộc tính về age khác nhau:
            name        age
            Fake         2
            Mickey       7
            Fuk          5
        - Sau đó, viết một hàm get_biggest_number(*args) nhận vào nhiều tham số, sau đó trả về số lớn nhất.
        - Và dựa trên hàm này, hay tìm và in ra có dạng như sau:
            The oldest dog is 7 years old.


Bài 02. Xem code đã có trong file btvn_02_pet.py.
    Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Hãy tạo ra class Pet để chứa các đối tượng của class Dog, class Pet này độc lập với class Dog (hay Pet ko kế thừa từ Dog)
        - Sau đó, tạo 4 đối tượng kiểu Dog và gán thành thuộc tính của 1 đối tượng kiểu Pet
            name        age
            Tom          6
            Jerry        9
            Butt         3
            Wine         1
        - Code đoạn chương trình để in ra được như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.

Bài 03. Sử dụng tiếp file btvn_02_pet.py sau khi đã code xong Bài 02.
    Giải quyết yêu cầu sau:
        - Thêm thuộc tính is_hungry = True cho class Dog
        - Thêm một method eat() để thay đổi giá trị cho is_hungry thành False khi nó được gọi đến
        - Kiểm tra và in ra
            My dogs are not hungry.
        nếu như tất cả các Dog trong Pet đều có is_hungry = False, ngược lại thì in ra
            My dogs are hungry.
        - Cuối cùng có thể in ra được kiểu như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.
            My dogs are not hungry.

Bài 04. Xem code đã có trong file btvn_04_dog_walking.py.
    Giải quyết yêu cầu sau:
        - Thêm method walk() vào class Pet và Dog. Khi gọi đến hàm walk() trong Pet thì vỡi mỗi đối tượng của Dog trong Pet
        sẽ gọi đến hàm walk() tương ứng.
        - Viết đoạn chương trình để in ra như sau:
            Tom is walking!
            Jerry is walking!
            Butt is walking!

Bài 05. Viết một class NewString trong đó có 2 phương thức: get_string() và print_string()
    - get_string - nhận một string do người dùng nhập vào
    - print_string - in string nhập vào ở dạng toàn chữ in hoa

Bài 06. Xây dựng class User để lưu trữ thông tin người dùng hệ thống
    - Thuộc tính: first_name, last_name, birthday, email, address, username, password
    - Hành vi (phương thức): login(), logout(), update_info()

"""