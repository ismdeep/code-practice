# coding: utf-8
# author: ismdeep
# dateime: 2019-04-15 14:31:37
# filename: test_ismdeep_utils.py
# blog: https://ismdeep.com

from ismdeep_utils import DateTime
import unittest
import random


class DateTimeTest(unittest.TestCase):

    def testDateTime(self):
        print(str(DateTime()))
        print(DateTime().timestamp())
        d = DateTime()
        print(str(d))
        d.parse_from_timestamp(d.timestamp() + 60 * 2)
        print(str(d))
        assert 5 == 5

    def testDateTime_parse_from_timestamp_to_datetime(self):
        for i in range(500):
            val = random.randint(0, 1555312301)
            d = DateTime()
            d.parse_from_timestamp(val)
            assert d.timestamp() == val


if __name__ == '__main__':
    unittest.main()

