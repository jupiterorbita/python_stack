#product

#attributes:
# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"

# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.


class product:
    def __init__(self,price=0,item_name='',weight=0,brand='',status='for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    
    def sell(self):
        self.status = 'SOLD'
        return self

    def addTax(self,tax=0.15):
        self.price = round(self.price * (1+tax))
        print('tax is ', 1+tax)
        # self.price *= 1.15
        return self

    def returnP(self,return_for_reason=0):
        if return_for_reason == 1:
            self.status = 'defective'
            discount = self.price * (20 / 100)
            self.price -= discount
            print('discount is ',discount)
        else:
            self.status = 'for sale'
        return self
    def displayinfo(self):
        print('All product details : ')
        print(self.__dict__)
        print('price is = ',self.price)
        print('item name is = ', self.item_name)
        print('product weight is = ',self.weight)
        print('brand name is = ',self.brand)
        print('product status = ',self.status)
        return self

# product().displayinfo()
# price, item_name, weight, brand, status
# product().displayinfo()
print('\n')

instance1 = product(1125,'Awesome product',125,'Super-Brand(R)')
instance1.addTax(0.15).sell().returnP(1).displayinfo()
# case1 = product().sell().displayinfo()
