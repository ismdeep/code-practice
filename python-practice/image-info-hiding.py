# coding:utf-8

from PIL import Image


def str_2_bin(_s_):
    _s_ = list(_s_.encode('utf-8'))
    ans = []
    _index_ = -1
    for item in _s_:
        for i in range(8):
            ans.append(item % 2)
            item >>= 1
    return ans


def main():
    im = Image.open('image.jpg')
    w, h = im.size
    info_size = int(w * h * 3 / 8)
    # s = input('enter your info({}B) to hide >> '.format(info_size))
    s = 'hello world.'
    bin = str_2_bin(s)
    print(*bin)
    (r, g, b) = im.getpixel((1, 1))
    print(r, g, b)
    # im.putpixel((4, 4), (0, 0, 0))
    # im.show()


main()
