foods =[]
prices =[]
total =0

while True :
     food = input("enter the food to buy and (q to  quit)")
     if food.lower() =="q":
          break
     else:
          price = float(input(f"enter the price of {food}: $"))
          foods.append(food)
          prices.append(price)

for food in foods:
     print(food ,end = "   ")
for price in prices :
    total +=price
print()
print (f"your total is {total}")