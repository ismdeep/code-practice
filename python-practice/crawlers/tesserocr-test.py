# coding: utf-8
# author: ismdeep
# dateime: 2019-04-07 22:31:19
# filename: tesserocr-test.py
# blog: https://ismdeep.com

import tesserocr
from PIL import Image

img = Image.open('/data/test.jpg')
text = tesserocr.image_to_text(img)
ans = ''
for item in text:
    if item in '0123456789':
        ans += item
print(ans)
