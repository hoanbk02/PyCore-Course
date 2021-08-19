""" Bước chuẩn bị. Tiến hành cài thêm package:
    pip install pywhatkit
    => Module chứa function chuyển đổi text sang chữ viết tay
"""

import pywhatkit

pywhatkit.text_to_handwriting(
    "pip install pywhat",
    rgb=[0, 0, 0]
)

