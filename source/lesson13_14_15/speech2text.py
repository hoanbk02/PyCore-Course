"""
Bước Chuẩn bị
    - Cài đặt module SpeechRecognition: pip install speechrecognition
    => Module thực hiện việc nhận dạng giọng nói và chuyển đổi thành văn bản
    - Cài đặc module PyAudio: pip install pyaudio
    => Module chấp nhận định dạng mặc định của tệp audio từ microphone
    Nếu khi cài bị error về portaudio thì giải quyết bằng cài: sudo apt-get install portaudio19-dev python-pyaudio
"""

import speech_recognition as s2t
import time


recognizer = s2t.Recognizer()
with s2t.Microphone() as micro:
    print('Speak ...')
    audio_input = recognizer.record(micro, duration=10)
    print("Recording time:", time.strftime("%I:%M:%S"))

    try:
        # Tham số language sẽ giúp recognizer làm việc chuẩn hơn
        text_output = recognizer.recognize_google(audio_input, language='vi-VN')
        print("Text recognize from audio:", text_output)
    except:
        print("Can't process the audio input!")

    print("Finished:",  time.strftime("%I:%M:%S"))
