first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


print('==='*20)

x = "hello world"
print(x.title())
# output:
# "Hello World"

print('==='*20)


list = [99,4,2,5,-3]
tuple = (99,4,2,5,-3)
print(list[:])
#the output would be [99,4,2,5,-3]
print(list[1:])
#the output would be [4,2,5,-3];
print(list[:4])
#the output would be [99,4,2,5]
print(list[2:4])
#the output would be [2,5];

print('==='*20)



capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}
# creating a new key/value pair
capitals["abc"] = "New Country" 
# updating
capitals["abc"] = "ABC Country"
#to print all keys
for data in capitals:
     print(data)
#another way to print all keys
for key in capitals.keys():
     print(key)
#to print the values
for val in capitals.values():
     print(val)
#to print all keys and values
for key, val in capitals.items():
     print(key, " = ", val)

print('==='*20)
