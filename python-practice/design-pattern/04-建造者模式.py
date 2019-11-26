# coding:utf-8


# 建造者基类
class PersonBuilder(object):
    def BuildHead(self):
        pass

    def BuildBody(self):
        pass

    def BuildArm(self):
        pass

    def BuildLeg(self):
        pass


# 胖子
class PersonFatBuilder(PersonBuilder):
    type = '胖子'

    def BuildHead(self):
        print('构建%s的头' % self.type)

    def BuildBody(self):
        print('构建%s的身体' % self.type)

    def BuildArm(self):
        print('构建%s的胳膊' % self.type)

    def BuildLeg(self):
        print('构建%s的脚' % self.type)


# 瘦子
class PersonThinBuilder(PersonBuilder):
    type = '瘦子'

    def BuildHead(self):
        print('构建%s的头' % self.type)

    def BuildBody(self):
        print('构建%s的身体' % self.type)

    def BuildArm(self):
        print('构建%s的胳膊' % self.type)

    def BuildLeg(self):
        print('构建%s的脚' % self.type)


# 指挥者
class PersonDirector(object):
    pb: PersonBuilder = None

    def __init__(self, pb):
        self.pb = pb

    def CreatePerson(self):
        self.pb.BuildHead()
        self.pb.BuildBody()
        self.pb.BuildArm()
        self.pb.BuildLeg()


def clientUI():
    pb = PersonThinBuilder()
    pd = PersonDirector(pb)
    pd.CreatePerson()

    pb = PersonFatBuilder()
    pd = PersonDirector(pb)
    pd.CreatePerson()
    return
