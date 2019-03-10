class User(object):
    __instance = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '''{"name": "%s"}''' % self.name

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.name = name
        return cls.__instance


user1 = User("Alice")
print("user1 address: {%s} str: %s" % (id(user1), str(user1)))
user2 = User("Bob")
print("user1 address: {%s} str: %s" % (id(user1), str(user1)))
print("user2 address: {%s} str: %s" % (id(user2), str(user2)))
