# coding: utf-8
# author: ismdeep
# datetime: 2019-04-15 14:31:37
# filename: test_ismdeep_utils.py
# blog: https://ismdeep.com

from ismdeep_utils import DateTime
from ismdeep_utils import Config
import unittest
import random


class DateTimeTest(unittest.TestCase):

    @staticmethod
    def testDateTime():
        print(str(DateTime()))
        print(DateTime().timestamp())
        d = DateTime()
        print(str(d))
        d.parse_from_timestamp(d.timestamp() + 60 * 2)
        print(str(d))
        assert 5 == 5

    @staticmethod
    def testDateTime_parse_from_timestamp_to_datetime():
        for i in range(500):
            val = random.randint(0, 1555312301)
            d = DateTime()
            d.parse_from_timestamp(val)
            assert d.timestamp() == val


class ConfigTester(unittest.TestCase):
    @staticmethod
    def testConfig():
        config = Config()
        config.put('path', '/data/tmp/config')
        config.put('thread-size', 10)
        print(config.dump())
        config.save(open('config.ini', 'w'))

    @staticmethod
    def testConfigLoad():
        config = Config()
        config.load(open('config.ini', 'r'))
        print(config.dump())

    @staticmethod
    def testConfigLoads():
        config = Config()
        s = open('config.ini', 'r').read()
        print(s)
        config.loads(s)
        print(config.dump())


if __name__ == '__main__':
    unittest.main()

