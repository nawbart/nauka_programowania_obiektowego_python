from abc import ABC, abstractmethod

class two_wheeler(ABC):

    def __init__(self, type, color, brand, gearbox):
        self.type = type
        self.color = color
        self.brand = brand
        self.gearbox = gearbox

    def mileage(self):
        return self.mileage()

    def go(self):
        self.mileage += 1

    class scooter(two_wheeler):

        def takePerson(self):
            print("Here is", self.type, "i can ride with two people." )



    classmotocross(two_wheeler):

    def jump(self):
        print("Here is", self.type, 'i can jump over huge things')