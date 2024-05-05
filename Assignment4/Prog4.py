a= eval(input ("Enter data :"))
search=eval(input("Searching element :"))
for i in a:
    if i==search:
        print ("Index of the element:",a.index(search))

    else:
        print("Searching element will be not found")



