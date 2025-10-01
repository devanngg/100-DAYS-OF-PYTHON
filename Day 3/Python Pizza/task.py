print("Welcome to Python Pizza Deliveries!")
grand_total=0
total1=0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
  print("You selected", size, "pizza.")
  total1=total1+15
elif size == "M":
  print("You selected", size, "pizza.")
  total1=total1+20
elif size == "L":
  print("You selected", size, "pizza.")
  total1=total1+25

total2=0
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    total2=total2+2
elif pepperoni == "N":
    total2=total2+0
total3=0

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    total3=total3+1
elif extra_cheese == "N":
    total3=total3+0

grand_total=total1+total2+total3
print("Your total is", grand_total)

