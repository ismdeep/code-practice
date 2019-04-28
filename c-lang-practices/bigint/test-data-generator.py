# coding:utf-8

import random

with open('test-add.dat', 'w') as f:
    for i in range(300):
        a = random.randint(-234987239487239479238472, 234987239487239479238472)
        b = random.randint(-234987239487239479238472, 234987239487239479238472)
        c = a + b
        f.write('%d %d %d\n' % (a, b, c))
print('=> test-add.dat generated')


with open('test-subtract.dat', 'w') as f:
    for i in range(300):
        a = random.randint(-234987239487239479238472, 234987239487239479238472)
        b = random.randint(-234987239487239479238472, 234987239487239479238472)
        c = a - b
        f.write('%d %d %d\n' % (a, b, c))
print('=> test-subtract.dat generated')


with open('test-multiply.dat', 'w') as f:
    for i in range(300):
        a = random.randint(-234987239487239479238472, 234987239487239479238472)
        b = random.randint(-234987239487239479238472, 234987239487239479238472)
        c = a * b
        f.write('%d %d %d\n' % (a, b, c))
print('=> test-multiply.dat generated')
