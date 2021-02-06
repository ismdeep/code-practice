#!/usr/bin/env python3

import sys
from PIL import Image
from progress.bar import IncrementalBar

level_val = [0xff, 0xfe, 0xfc, 0xf8, 0xf0, 0xe0, 0xc0, 0x80]


def show_help():
    print('''Usage: python3 remove-privacy-from-pic.py picture_path [level]
    level: remove level, from 0 to 7''')


def convert_to_dest_path(__path__, __remove_level__):
    items = __path__.split('.')
    items[len(items) - 2] = items[len(items) - 2] + "_privacy_removed_" + str(__remove_level__)
    return '.'.join(items)


def remove_privacy(__source_pic_path__, __dest_pic_path__, __level__):
    img = Image.open(__source_pic_path__)
    width, height = img.size
    # decide what size should be
    if width > 1024:
        r = 1024.0 / width
        width = int(width * r)
        height = int(height * r)
    if height > 1024:
        r = 1024.0 / height
        width = int(width * r)
        height = int(height * r)
    img = img.resize((width, height), Image.ANTIALIAS)

    mode = img.mode
    dest_img = Image.new(mode, (width, height), (0, 0, 0))
    bar = IncrementalBar('Processing', max=width, width=50, suffix='%(percent)d%%')
    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))
            r &= level_val[__level__]
            g &= level_val[__level__]
            b &= level_val[__level__]
            dest_img.putpixel((i, j), (r, g, b))
        bar.next()
    bar.finish()
    dest_img.show()
    dest_img.save(__dest_pic_path__)


def main():
    if len(sys.argv) <= 1:
        show_help()
        exit(-1)
    picture_path = sys.argv[1]
    remove_level = 3
    if len(sys.argv) > 2:
        remove_level = int(sys.argv[2])
    if remove_level < 0 or remove_level > 7:
        show_help()
        exit(-1)
    picture_dest_path = convert_to_dest_path(__path__=picture_path, __remove_level__=remove_level)
    remove_privacy(__source_pic_path__=picture_path, __dest_pic_path__=picture_dest_path, __level__=remove_level)


if __name__ == '__main__':
    main()
