a =input("Enter a list")
number= [int(num) for num in a.split(',')]
sum =0
for num1 in number:
    sum +=num1
print(sum)
