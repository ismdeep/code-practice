class AbstractPerson(object):
    """人基类"""
    road = None

    def drive(self):
        pass


class AbstractRoad(object):
    """公路基类"""
    car = None


class AbstractCar(object):
    """车辆基类"""

    def run(self):
        pass


class Man(AbstractPerson):
    def drive(self):
        print("男人开着", end='')
        self.road.run()


class Woman(AbstractPerson):
    def drive(self):
        print("女人开着", end='')
        self.road.run()


class Street(AbstractRoad):
    """市区街道"""

    def run(self):
        self.car.run()
        print("在市区街道上行驶")


class SpeedWay(AbstractRoad):
    """高速公路"""

    def run(self):
        self.car.run()
        print("在告诉公路上行驶")


class Car(AbstractCar):
    """小汽车"""

    def run(self):
        print("小汽车在", end='')


class Bus(AbstractCar):
    """公共汽车"""

    def run(self):
        print("公共汽车在", end='')


if __name__ == '__main__':
    '''小汽车在高速公路上行驶'''
    p = Man()
    p.road = SpeedWay()
    p.road.car = Car()
    p.drive()
