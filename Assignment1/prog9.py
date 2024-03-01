year= int(input("Enter the year:"))
month =int(input("Enter the month:"))
if((month==2 )) :
    if(year %4 ==0):
      if(year %100 ==0):
        if(year %400 ==0):
         print("")

    print("Number of days are 29")
elif(month==2):
    print("Number of days is 28")

elif(month ==1 or month ==3 or month == 5 or month == 7 or month==8 or month ==10 or month == 12):
    print("Number of days is 31")
else:
    print("Number of days is 30")