"""
Bước Chuẩn bị. Đối với TTS offline, thì có pyttsx3 là thư viện dựa trên TTS engine được cài đặt trong OS
    - Tài liệu:
        https://github.com/nateshmbhat/pyttsx3
        https://pyttsx3.readthedocs.io/en/latest/
    - Cài đặt module pyttsx3: pip install pyttsx3
    - Trên Ubuntu cần cài đặt: sudo apt-get install espeak python-espeak
"""

import pyttsx3


engine_tts = pyttsx3.init()
txt = """
Xin chào các bạn! Bài khó thế nhỉ. Quật đầu vào tường chết đây!
"""
voice_vn = 'vietnam'
# voice_vn_sg = 'vietnam_sgn'
# voice_vn_hue = 'vietnam_hue'
engine_tts.setProperty('voice', voice_vn)
engine_tts.setProperty('rate', 120)

# engine_tts.say(txt)
engine_tts.save_to_file(txt, 'offline.mp3')

# Lấy các voices khả dụng ra để thực hiện tổng hợp
# voices = engine_tts.getProperty('voices')
# for voice in voices:
#     engine_tts.setProperty('voice', voice.id)
#     engine_tts.say('The quick brown fox jumped over the lazy dog.')

engine_tts.runAndWait()


# Lấy danh sách các voice khả dụng
# voices = engine_tts.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
