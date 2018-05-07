#For Loop Basic I

#basic
#print all the numbers/integers from 0 to 150
for a in range(0,151):
    print('printing a ',a)

#multiples of 5
for b in range(5,105):
    if b%5==0:
        print('multiples of 5 are ',b)

#counting, the dojo way
#Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for i in range(1,100):
    if i%5==0:
        print(i,'coding')
    if i%10==0:
        print('dojo')
    else:
        print(i)

# Whoa. That Sucker's Huge
#Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0,500):
    if x%2!=0:
        print(x)
        sum+=x
        print('sum is',sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for c in range(2018,0,-4):
    print(c)
    
#Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 9 6 3 (on successive lines)
def flexCount(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i%mult==0:
            print(i)

flexCount(2,100,5)
