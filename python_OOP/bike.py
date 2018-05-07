#http://learn.codingdojo.com/m/72/5471/35330
#Assignment: Bike

# Create a new class called Bike with the following properties/attributes:
# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() method to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.
# Add the following methods to this class
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
# What would you do to prevent the instance from having negative miles?
# Which methods can return self in order to allow chaining methods?
class bike:
    def __init__(self, o_price=0, max_speed=0, miles=0):
        self.price = o_price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print(self.price)
        print(self.max_speed)
        print(self.miles)
        return self
    def ride(self):
        print('riding')
        self.miles += 10
        return self
    def reverse(self):
        print('reversing')
        self.miles -= 5
        return self

instance1 = bike() #ride 3 times, rev once )
instance1.ride().ride().ride().reverse().displayinfo()

instance2 = bike()
instance2.ride().ride().reverse().reverse().displayinfo()

instance3 = bike()
instance3.reverse().reverse().reverse().displayinfo()

# bike.displayinfo(123,123,123)
# or
# instance1.displayinf(123,123,123)


    