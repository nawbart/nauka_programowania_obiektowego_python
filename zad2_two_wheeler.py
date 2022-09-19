from abc import ABC, abstractmethod

class two_wheeler(ABC):

    def __init__(self, color, brand, gearbox):
        self.color = color
        self.brand = brand
        self.gearbox = gearbox

    def mileage(self):      #przebieg
        return self.mileage()

    def go(self):       #metoda jedz, powodujaca zwiekszanie sie przebiegu
        self.mileage += 1

    @abstractmethod
    def giveData(self):         #abstrakcyjna metoda podaj dane
        pass

    class scooter(two_wheeler):

        def __init__(self, color, brand, gearbox, trunk):     #trunk - bagaznik
            super().__init__(color, brand, gearbox)
            self.trunk = trunk

        def takePerson(self):
            print("Here is", self.type, "i can ride with two people." )



    class motocross(two_wheeler):

        def __init__(self, color, brand, gearbox, approval):      #approval - homologacja
            super().__init__(color, brand, gearbox)
            self.approval = approval
        def jump(self):
            print("Here is", self.type, 'i can jump over huge things')