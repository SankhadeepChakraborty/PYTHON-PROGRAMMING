tup=eval(input("1st tupple : "))
tup2=eval(input("2nd tuple : "))
res=tuple(x+y for x,y in zip(tup,tup2))
print("Add two tupples : ",res)