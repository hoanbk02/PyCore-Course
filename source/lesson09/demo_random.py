# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"


# Ví dụ: Mô phỏng tung xúc xắc. In ra số chấm trên mặt sau khi tung một xúc xắc 10 lần
""" Để mô phỏng được yếu tố may rủi (ngẫu nhiên) thì chúng ta có thể dùng đến module random"""
import random

for roll in range(10):
    print(random.randrange(1, 7), end=' ')

# Tìm hiểu chi tiết về hàm randrange(start, stop=None, step=1)

# Ví dụ: Kiểm tra xem khả năng (hay xác suất) xảy ra của các mặt có phải thực sự ngẫu nhiên hay không
""" Để làm được việc trên hãy tung một xúc xắc càng nhiều lần càng tốt"""

import random

# Các biến lưu số lần xuất hiện của các mặt
f1 = f2 = f3 = f4 = f5 = f6 = 0

n = int(input('Muốn tung bao lần: '))

for roll in range(n):
    num = random.randrange(1, 7)

    if num == 1:
        f1 += 1
    elif num == 2:
        f2 += 1
    elif num == 3:
        f3 += 1
    elif num == 4:
        f4 += 1
    elif num == 5:
        f5 += 1
    elif num == 6:
        f6 += 1

print(f'Số chấm{"Số lần":>13}{"Xác suất":>15}')
print(f'{1:>7}{f1:>13}{round(f1/n, 5):>15}')
print(f'{2:>7}{f2:>13}{round(f2/n, 5):>15}')
print(f'{3:>7}{f3:>13}{round(f3/n, 5):>15}')
print(f'{4:>7}{f4:>13}{round(f4/n, 5):>15}')
print(f'{5:>7}{f5:>13}{round(f5/n, 5):>15}')
print(f'{6:>7}{f6:>13}{round(f6/n, 5):>15}')


""" Bài tập. Mô phỏng lại trò chơi sau: 
- Người chơi tung 2 con xúc xắc 6 mặt, các mặt có số chấm là: 1, 2, 3, 4, 5, 6
- Quan sát kết quả, tính tổng các mặt hướng lên sau khi 2 con xúc xắc đứng yên
- Lần đầu tiên,
    - Nếu tổng là 7 hoặc 11 => Người chơi THẮNG
    - Nếu tổng là 2, 3 hoặc 12 => Người chơi THUA
    - Nếu tổng là 4, 5, 6, 8, 9 hoặc 10 => Đây sẽ là ĐIỂM của người chơi, và sang vòng tiếp theo
- Để giành được THẮNG, người chơi tiếp tục tung 2 con xúc xắc cho đến khi ra được tổng = ĐIỂM trong lần đầu tiên; 
nếu tung ra được tổng = 7 => Người chơi THUA
"""

import random

THANG = (7, 11)
THUA = (2, 3, 12)


def rolling_dice():
    """ Tung hai xúc xắc, in ra kết quả và trả về tổng """
    num1 = random.randrange(1, 7)
    num2 = random.randrange(1, 7)
    num_sum = num1 + num2
    print(f'Tung ra: {num1} + {num2} = {num_sum}')
    return num_sum


# Lần chơi đầu tiên
player_point = rolling_dice()
if player_point in THANG:
    game_status = 'THANG'
elif player_point in THUA:
    game_status = 'THUA'
else:
    game_status = 'TIEP_TUC'
    print(f'Số ĐIỂM = {player_point}')

# Tiếp tục chơi đến khi THẰNG hoặc THUA
while game_status == 'TIEP_TUC':
    sum_of_dice = rolling_dice()

    if sum_of_dice == player_point:
        game_status = 'THANG'
    elif sum_of_dice == 7:
        game_status = 'THUA'

# In ra kết quả cuối cùng của người chơi
if game_status == 'THANG':
    print('Người chơi đã THẮNG')
else:
    print('Người chơi đã THUA')
