""" Bước chuẩn bị. Đối với TTS online, một trong những service phổ biến là dùng Google Text to Speech
    - Cài module Google Text to Speech: pip install gTTS
    => Module tổng hợp tiếng nói từ văn bản
    - Cài module playsound: pip install playsound
    => Module chạy tệp tin âm thanh mp3

    - Nếu khi chạy bị lỗi "No module named 'gi'" thì tiến hành:
        + Cài 2 module:
            pip install vext
            pip install vext.gi
        + Cài thêm: sudo apt-get install gstreamer-1.0
"""

import gtts
from playsound import playsound


# Danh sách các ngôn ngữ được hỗ trợ
# print(gtts.lang.tts_langs())

txt = """
Giá Bitcoin hôm nay là ₫1.114.974.012 VND với khối lượng giao dịch trong 24 giờ là ₫666.291.088.350.408 VND.
"""
tts = gtts.gTTS(txt, lang='vi')
tts.save('online.mp3')
playsound('online.mp3')
