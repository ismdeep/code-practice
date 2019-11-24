# coding:utf-8


class Shape(object):
    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print("draw circle")


class Square(Shape):
    def draw(self):
        print("draw square")


class Rectangle(Shape):
    def draw(self):
        print('draw rectangle')


class ShapeFactory(object):
    def getShape(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None


fac = ShapeFactory()
obj = fac.getShape('Circle')
obj.draw()

