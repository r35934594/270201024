age=int(input("please enter your age:"))
ticket=3
discount=0.5
if age<6 or age>60:
  print("free")
elif age>6 and age<18:
  print(ticket*(1-discount))
else:
  print(ticket)