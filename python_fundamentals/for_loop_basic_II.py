#For Loop Basic II
print('---1---')
#1 Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig(arr):
    for i in range(0,len(arr)):
        if arr[i]<1:
            arr[i] = 'big'
    return arr

print(makeItBig([-1,3,5,-5]))

print('---2---')
#2 Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1,1]) changes array to [-1,1,1,3] and returns it

def countPositives(arr1):
    count =0
    for b in range(0,len(arr1)):
        # print(b)
        if arr1[b] > 0:
            # print('arr1[b] is greater than 0',arr1[b])
            count+=1
            # print('count ',count)
        arr1[len(arr1)-1] = count
        # print(arr1)
    return arr1

print(countPositives([-1,1,1,1]))

print('---3---')
#3 SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr2):
    sum=0
    # for c in range(0, len(arr2)+1):
    for c in arr2:
        # print(c)
        sum+=c
    print('sum is = ',sum)
sumTotal([1,2,3,4])

print('---4---')
#4 Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def multiples(arr3):
    sum=0
    avg=arr3[0]
    for d in range(0,len(arr3)):
        # print('this is d ',d)
        sum = sum + arr3[d]
        # print('sum inside ',sum)
    # print(sum)
    avg = sum / len(arr3)
    print('avg ',avg)

multiples([1,2,3,4]) #should return 2.5

print('---5---')
#5 Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

def length(arr4):
    # print(arr4)
    print('length is = ',len(arr4))
    return len(arr4)

length([1,2,3,4])

print('---6---')
#6 Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimumN(arry):
    # print(arry)
    min = arry[0]
    print('length is ',len(arry))
    if (len(arry) == 1): 
        print('fail')
        return False    # it is not returning false!!!
    for i in range(0, len(arry)):
        # print('this is index ',i)
        if i>arry[i]:
            min = arry[i]
    print('min num is ',min)

minimumN([1,3,4,5])

print('---7---')
# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
def maximumN(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        # print(i)
        if max<arr[i]:
            max = arr[i]
            # print(max)
    print(max)

maximumN([-1,-2,-3,-4])

print('---8---')
#8 UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def ultimate(arr):
    sum = 0
    avg = arr[0]
    min = arr[0]
    max = arr[0]

    for i in range(0, len(arr)):
        sum += arr[i]
        if min > arr[i]:
            min = arr[i]
        if max < arr[i]:
            max = arr[i]
    avg = sum / len(arr)

    dictionary = {
        "sumTotal":sum,
        "average":avg,
        "min":min,
        "max":max,
        "length of the list": len(arr)
    }
    print(dictionary)

ultimate([1,2,3,4,5])

print('---9---')
#9 ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# INCOMPLETE

def revList(arr):
    temp = 0
    for i in range(0, int(len(arr)/2)):
        temp = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = arr[i]
        arr[i] = temp
    print(arr)

revList([1,2,3,4]) #should return [4,3,2,1]