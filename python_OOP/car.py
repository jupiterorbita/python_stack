
import random

class car:
    def __init__(self,price=0, speed=0, fuel=0, mileage=0, tax=0.12):
        self.price = price
        self.speed = str(speed)+' mph'
        self.fuel = fuel
        self.mileage = str(mileage)+' mpg'
        self.tax = tax
        if self.price > 10000:
            print('price over 10,000 -> tax is 15% ')
            self.tax = 0.15
        else:
            print('price below 10,000 -> tax is 12% ')
        #fuel
        if self.fuel < 0.25:
            self.fuel = 'empty'
        elif self.fuel >= 0.25:
            self.fuel = 'not full'
        elif self.fuel >= 0.5:
            self.fuel = 'kind of full'
        else: 
            self.fuel = 'full'

    def display_all(self):
        print('price ',self.price)
        print('speed ',self.speed)
        print('fuel ',self.fuel)
        print('mileage ',self.mileage)
        print('tax ',self.tax)
        return self

    # def printALL(self):
    #     print(self.__dict__)

# instance1.display_all()
instance1 = car(2000, 35, 1, 15) #price,speed,fuel,mileage
instance2 = car(2000, 5, 0.25, 105)
instance3 = car(2000, 15, 0.1, 95)
instance4 = car(2000, 25, 0.7, 25)
instance5 = car(2000, 35)
instance6 = car(2000000, 15)
print('\n')
instance1.display_all()
print('\n')
instance2.display_all()
print('\n')
instance3.display_all()
print('\n')
instance4.display_all()
print('\n')
instance5.display_all()
print('\n')
instance6.display_all()

# print(instance1.__dict__) #returns all valies in a dict