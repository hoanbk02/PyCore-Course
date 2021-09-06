"""" Nhắc nhở uống nước:
    - Chạy trên macOS mà không cần cải đặt thêm gì.
    - Với windows thì tham khảo thêm package: win10toast
    - Lấy code của emoji tại: https://unicode.org/emoji/charts/emoji-list.html
"""

import os
import datetime
import time


def gen_notify(title, text, sound="default"):
    cmd = f"""osascript -e 'display notification "{text}" with title "{title}" sound name "{sound}"'"""
    os.system(cmd)


def input_time():
    hours = int(input('Giờ: '))
    minutes = int(input('Phút: '))
    seconds = int(input('Giây: '))
    interval = seconds + (minutes*60) + (hours*3600)
    print(f'Khoảng thời gian bạn chọn là: {interval} giây')
    return interval


def log():
    time_now = datetime.datetime.now()
    time_now_str = time_now.strftime('%H:%M:%S')
    with open('log.txt', 'a') as f:
        f.write(f'Đã uống nước vào lúc: {time_now_str}\n')


def start_time(interval):
    while True:
        gen_notify(
            '\N{alarm clock} Uống nước đeeeeeeê!',
            '\U0001F595 \U0001F449 Đã đến lúc uống nước \U0001F964 rồi đó mày ơi!\n\U0001F60E Không đừng trách tao \U0001F5E1')
        log()
        time.sleep(interval)


if __name__ == '__main__':
    time_interval = input_time()
    start_time(time_interval)
