#compund intresst 
principle =0
rate =0
time =0
while principle <=0:
    principle= float(input ("entert the initial amount"))
    if principle<=0:
        print("principle cant be zero")


while rate <=0:
    rate= float(input ("entert the initial intrest"))
    if rate<=0:
        print("rate cant be zero")


while time<=0:
    time= float(input ("entert the time in yrs"))
    if time<=0:
        print("time cant be zero")
total = round(principle *pow((1+rate/100),time),1)
print(f"your balance after the {time} years of the the {principle}with {rate } is :{total}")