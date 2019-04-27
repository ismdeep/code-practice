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


def hide_info():
    im = Image.open('/Users/ismdeep/Pictures/13984167,1920,1080.jpg')
    w, h = im.size
    info_size = int(w * h * 3 / 8)
    s = input('enter your info({}B) to hide >> '.format(info_size))
    slen = len(list(s.encode('utf-8')))
    bin2 = str_2_bin(s)
    bin_str = []
    for i in range(32):
        bin_str.append(slen % 2)
        slen >>= 1
    for item in bin2:
        bin_str.append(item)
    c = []
    tmp = []
    for i in range(len(bin_str)):
        tmp.append(bin_str[i])
        if len(tmp) >= 3:
            c.append(tmp)
            tmp = []
    if len(tmp) > 0:
        while len(tmp) < 3:
            tmp.append(0)
        c.append(tmp)
    i, j = 0, 0
    for lsr, lsg, lsb in c:
        (r, g, b) = im.getpixel((i, j))
        r = (r >> 1 << 1) + lsr
        g = (g >> 1 << 1) + lsg
        b = (b >> 1 << 1) + lsb
        im.putpixel((i, j), (r, g, b))
        j += 1
        w += int(j / h)
        j %= h
    # im.show()
    im.save('/Users/ismdeep/Desktop/tmp.png', 'PNG')


def read_info():
    im = Image.open('/Users/ismdeep/Desktop/info.png')
    w, h = im.size
    a = []
    for i in range(w):
        for j in range(h):
            (r, g, b) = im.getpixel((i, j))
            a.append(r % 2)
            a.append(g % 2)
            a.append(b % 2)
    slen = 0
    for i in range(32):
        slen <<= 1
        slen += (a[31 - i] % 2)
    _index_ = 0
    b = bytearray()
    for i in range(slen):
        val = 0
        for j in range(_index_ + 7, _index_ - 1, -1):
            val <<= 1
            val += a[j + 32]
        b.append(val)
        _index_ += 8
    s = b.decode('utf-8')
    print(s)


def main():
    # hide_info()
    read_info()


main()
