weight = float(input("enter your weight"))
unit  = input("kg or pounds")
if unit =="k":
    weight = weight *2.205
    unit = "lbs"
    print(f"your weight is : {weight} {unit}")
elif unit == "l":
    weight = weight /2.205
    unit="kgs"
    print(f"your weight is : {weight} {unit}")
else :
    print(f"{unit} was not valid")

