import math
number = int(input("Enter the number to check number"))
temp = number
sum = 0
while temp>0:
    fact =1
    i=1
    rem= temp % 10
    fact = math.factorial(rem)
    sum = sum+fact
    temp = temp //10
    if sum == number:
        print ("%d is a krishnomurti number"%number)
    else:
        print("%d is not a krishnomurti number"%number)
