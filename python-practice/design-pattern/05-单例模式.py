# coding:utf-8


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


a = MyClass("Alex")
b = MyClass("Jack")
print(a.name)
print(b.name)
