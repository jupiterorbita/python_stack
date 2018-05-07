#MathDojo

# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
# Then create a new instance called md. It should be able to do the following task:
# md.add(2).add(2,5,1).subtract(3,2).result
# which should perform 0+2+(2+5+1)-(3+2) and return 5.

class MathDojo:
    def __init__(self,parameter1=0,parameter2=0, parameter3=0):
        self.num1 = parameter1
        self.num2 = parameter2
        self.num3 = parameter3
        self.sum = 0
        self.result = parameter3
    def add(self,num1=0,num2=0,num3=0):
        self.sum = num1 + num2 + num3
        return self
    def subtract(self,num1=0,num2=0):
        self.sum = num1 - num2
        return self

# print(MathDojo(1,2).__dict__)
myMathObj = MathDojo()

print('MathDojo() default values =',myMathObj.__dict__)

md = MathDojo()
md.add(2).add(2,5,1).subtract(3,2)

def varargs(arg1, *args):
    print("Got "+arg1+" and "+ ", ".join(args))
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"

class Person:
  def pay_bill(self):
      raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
  def pay_bill(self):
      print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
  def pay_bill(self):
      print("Can I owe you ten bucks or do the dishes?")