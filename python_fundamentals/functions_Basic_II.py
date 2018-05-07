# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  How long is this array?
# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False
# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.

# countdown
# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  How long is this array?


def coundDown(num):
    newlist = []
    for i in range(num, -1, -1):
        print(i)
        newlist.append(i)
    return newlist


print(coundDown(20))


# Print and Return
def printAndReturn(list):
    print(list[0])
    return(list[1])


print('print and return', printAndReturn([11, 22]))

# first plus length


def sumFunc(arr):
    sum = arr[0] + len(arr)
    return sum


print('first plus length', sumFunc([100, 500000]))

# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False
# incomplete
# Values Greater than Second
def somefun(arr1):
    newarr1 = []
    count = 0
    if (len(arr1) == 1):
        return False
    else:
        for k in range(0, len(arr1)):
            print(k)
            if arr1[1] < arr1[k]:
                newarr1.insert(count,(arr1[k]))
                count += 1
        print(newarr1)
        print('values greater are ', count, 'values')

somefun([11, 22, 33,44,55])

# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.
def twonums(num1,num2):
    newarr2 = []
    for i in range(0,num1):
        # print(k)
        newarr2.append(num2)
        # print(newarr2)
    if len(newarr2) == num2:
        print('jinx')
    return (newarr2)

print(twonums(2,4))
