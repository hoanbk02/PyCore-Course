""" Bước chuẩn bị. Tiến hành cài thêm package:
    pip install pywhatkit
    => Module chứa function chuyển đổi text sang chữ viết tay
"""

import pywhatkit

pywhatkit.text_to_handwriting(
    "This is the base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes. For, user-defined classes, Exception is used. This class is responsible for creating a string representation of the exception using str() using the arguments passed. An empty string is returned if there are no arguments.",
    rgb=[0, 0, 0]
)
