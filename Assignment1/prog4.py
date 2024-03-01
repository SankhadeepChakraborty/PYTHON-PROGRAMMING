year= int(input("Enter your age :"))
if (year ==0 and year ==5):
    print("You are under the infant category")
elif(year >5 and year ==12):
     print("You are under the child category")
elif(year >12 and year ==17):
      print("You are under the teenager category")
elif(year >17 and year <=60):
      print("You are under the adult category")
else:
      print("You are under the senior citizen category")