

class animal:
    def __init__(self,name='animal',health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        print('animal walk -1 health ',self.health)
        return self
    def run(self):
        self.health -= 5
        print('animal run -5 health ',self.health)
        return self
    def displayhealth(self):
        print('display health = ',self.health)
        return self
        
instance_animal = animal().walk().walk().walk().run().run().displayhealth()
print('---- dog ----')
#dog class

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
class dog(animal):
    def __init__(self):
        super().__init__('dog',150)
    def pet(self):
        self.health +=5
        print('dog health is now +5 ',self.health)
        return self

myDogObj = dog()
print(myDogObj.__dict__)
myDogObj.walk().run().run().pet().displayhealth()
print('---- dragon ----')

class dragon(animal):
    def __init__(self):
        super().__init__('dragon',170)
    def fly(self):
        self.health -= 10
        print('flying is -10 health ',self.health)
        return self
    def displayhealth(self):
        print('i am a dragon')

myDragonObj = dragon()
print(myDragonObj.__dict__)
myDragonObj.fly().displayhealth()
