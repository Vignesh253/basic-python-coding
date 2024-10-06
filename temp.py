unit = input(" is this in the c or far :")
temp =float(input("enter th etemp"))

if unit=="c":
    temp =round ((9*temp/5+32))
    print (f"temp in far{temp}")
elif unit =="f":
    temp = round(temp-32*5/9,1)
    print (f"temp in c{temp}")
else :
    print(f"{unit} is not a valid ")