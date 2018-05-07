# Create beCheerful().  Within it, print string "good morning!" 98 times.
print("*"*80)

def beCheerful(name='', repeat=98):
	print(f"good morning {name}\n"*repeat)

beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")

# helpful tips for the next assignment
import random

print(random.random()) # returns a random floating number between 0.000 to 1.000
print(random.random()*50) # returns a float between 0.000 to 50.000
int( 3.654 ) # returns 3
round( 3.654 ) # returns 4

print("=="*30)


# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().



def randInt(min=0,max=100):
    if min>0:
        z = int(random.random()*max/2+min)
    else:
        z = int(random.random()*max+min)
    # z = random.random()*x+y
    print(f'random from {min}-{max} : ',z)


randInt(0,100)
randInt(0,50)
randInt(50,100)
randInt(50,500) #doesnt work


# randInt(int(random.random()*100), int(random.random()*50)) #returns a random integer between 0 to 100
# randInt() #returns a random integer between 0 to 50
# randInt(random.random()*100+50)#returns a random integer between 50 to 100
# #returns a random integer between 50 and 500
# print(random.random()*100/2+50)
# print(random.random()*500+50)