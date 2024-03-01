a= float(input("Enter 1st length of triangle:"))
b= float(input("Enter 2nd length of triangle::"))
c= float(input("Enter 3rd length of triangle::"))
if ( ((a+b)>c) and ((a+c)>b) and ((b+c)>a)) :
    if a==b==c:
        print ("Equilateral triangle")
    elif a==b or b==c or c==a :
        print("Isosceles triangle")
    else:
        print("Scalene triangle") 
else :
    print("Invalid")