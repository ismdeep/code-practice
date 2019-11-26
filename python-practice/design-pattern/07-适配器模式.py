# coding:utf-8


def printInfo(info):
    print(info)


# 球员类
class Player():
    name = ''

    def __init__(self, name):
        self.name = name

    def Attack(self):
        pass

    def Defense(self):
        pass


# 前锋
class Forwards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("前锋%s 进攻" % self.name)

    def Defense(self):
        printInfo("前锋%s 防守" % self.name)


# 中锋
class Center(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("中锋%s 进攻" % self.name)

    def Defense(self):
        printInfo("中锋%s 防守" % self.name)


# 后卫
class Guards(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def Attack(self):
        printInfo("后卫%s 进攻" % self.name)

    def Defense(self):
        printInfo("后卫%s 防守" % self.name)


# 外籍中锋（待适配类）
# 中锋
class ForeignCenter(Player):
    name = ''

    def __init__(self, name):
        Player.__init__(self, name)

    def ForeignAcctack(self):
        printInfo("外籍中锋%s 进攻" % self.name)

    def ForeignDefense(self):
        printInfo("外籍中锋%s 防守" % self.name)


# 翻译（适配类）
class Translator(Player):
    foreign_center = None

    def __init__(self, name):
        self.foreign_center = ForeignCenter(name)

    def Attack(self):
        self.foreign_center.ForeignAcctack()

    def Defense(self):
        self.foreign_center.ForeignDefense()


def clientUI():
    b = Forwards("巴蒂尔")
    ym = Guards("姚明")
    m = Translator("麦克格雷迪")

    b.Attack()
    m.Defense()
    ym.Attack()
    ym.Defense()


clientUI()
