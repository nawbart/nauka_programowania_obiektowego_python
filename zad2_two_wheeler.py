from abc import ABC, abstractmethod

class TwoWheeler(ABC):

    def __init__(self, color: str, brand: str, gearbox: str):
        self.color = color
        self.brand = brand
        self.gearbox = gearbox

    def mileage(self):      #przebieg
        return self.mileage()

    def go(self):       #metoda jedz, powodujaca zwiekszanie przebiegu o 1
        self.mileage += 1

    @abstractmethod
    def giveData(self):         #abstrakcyjna metoda podaj dane
        pass

class Scooter(TwoWheeler):

    def __init__(self, color, brand, gearbox, trunk: bool):     #trunk - bagaznik
        super().__init__(color, brand, gearbox)
        self.trunk = trunk

    def takePerson(self):
        print('Here is scooter, i can ride with two people.')

    def giveData(self):
        print(self.brand, self.color, self.gearbox, self.trunk)
        pass

    def set_color(self, color):
        self.color = color


class Motocross(TwoWheeler):

    def __init__(self, color, brand, gearbox, approval: bool):      #approval - homologacja
        super().__init__(color, brand, gearbox)
        self.approval = approval
    def jump(self):
        print('Here is cross i can jump over huge things')

    def giveData(self):
        print(self.brand, self.color, self.gearbox, self.approval)
        pass

def main():
    skuter = Scooter('red', 'aprilia', 'automatic', True)
    kros = Motocross('orange', 'KTM', 'manual', False)
    skuter.set_color('green') # ten sposob jest lepszy do zmiany koloru niż ten ponizej
    skuter.color = 'pink' # mozna ale sie nie powinno
    skuter.giveData()
    kros.giveData()
    pass

if __name__ == '__main__':
    main()



