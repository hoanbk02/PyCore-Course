"""
Bước Chuẩn bị
    - Cài đặt các thư viện:
        sudo apt-get update
        sudo apt-get install tesseract-ocr
        sudo apt-get install libtesseract-dev
    - Cài đặt module Python-tesseract: pip install pytesseract
    => Module thực hiện việc nhận dạng chữ trong ảnh và chuyển đổi thành văn bản
"""

import pytesseract
from PIL import Image


path_image = '???'
image = Image.open(path_image)
txt = pytesseract.image_to_string(image)
print("Văn bản có trong ảnh:")
print(txt)
