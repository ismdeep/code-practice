class AbstractCPU(object):
    series_name = ''


class AbstractFactory(object):
    computer_name = ""

    def createCPU(self):
        raise NotImplementedError

    def createMainBoard(self):
        raise NotImplementedError


class AbstractMainBoard(object):
    series_name = ''


class AMDCPU(AbstractCPU):
    def __init__(self, series):
        self.series_name = series


class AMDMainBoard(AbstractMainBoard):
    def __init__(self, series):
        self.series_name = series


class AMDFactory(AbstractFactory):
    computer_name = 'AMD 4 computer'

    def createCPU(self):
        return AMDCPU('amd444')

    def createMainBoard(self):
        return AMDMainBoard('amd400')


class IntelCPU(AbstractCPU):
    def __init__(self, series):
        self.series_name = series


class IntelMainBoard(AbstractMainBoard):
    def __int__(self):
        pass

    def __init__(self, series):
        self.series_name = series


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer'

    def createCPU(self):
        return IntelCPU('I7-6500')

    def createMainBoard(self):
        return IntelMainBoard('Intel-6000')


class ComputerEngineer(object):
    def makeComputer(self, factory_obj):
        self.prepareHardwares(factory_obj)

    def prepareHardwares(self, factory_obj):
        self.cpu = factory_obj.createCPU()
        self.mainboard = factory_obj.createMainBoard()

        info = """-------------- computer %s info:\ncpu: %s\nmainboard: %s""" % (
            factory_obj.computer_name, self.cpu.series_name, self.mainboard.series_name
        )
        print(info)


if __name__ == '__main__':
    engineer = ComputerEngineer()
    intel_factory = IntelFactory()
    engineer.makeComputer(intel_factory)

    amd_factory = AMDFactory()
    engineer.makeComputer(amd_factory)
