from abc import ABC, abstractmethod

class two_wheeler(ABC):

    def __init__(self, type, color, brand, gearbox):
        self.type = type
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

        def takePerson(self):
            print("Here is", self.type, "i can ride with two people." )



    class motocross(two_wheeler):

        def jump(self):
            print("Here is", self.type, 'i can jump over huge things')