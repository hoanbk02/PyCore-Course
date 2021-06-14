""" Bước chuẩn bị. Tiến hành cài thêm package:
    pip install pywhatkit
    => Module chứa function chuyển đổi text sang chữ viết tay
"""

import pywhatkit

pywhatkit.text_to_handwriting(
    "We thought this post to be very important for any student, so we are reposting it. Get Python handwritten notes, visit link in bio. Visit our site for free project source codes-- copyassignment.com. Turn on post notifications for more such posts like this.",
    rgb=[0, 0, 0]
)

