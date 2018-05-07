# http://learn.codingdojo.com/m/72/5471/35326

# class User:
#     name="Anna"
# anna = User()
# print("anna's name:", anna.name)                            
# User.name = "Bob"
# print("anna's name after change:", anna.name)               
# bob = User()
# print("bob's name:", bob.name)     

class User:
    def __init__(self, name, email):
        #instance vars
        self.name= name
        self.email=email
        self.logged=False

    #method
    def login(self):
        self.logged=True
        print(self.name + ' is logged in')
        return self

#instance of the class
new_user=User("Anna","anna@email.com")
print(new_user.name,new_user.email)



