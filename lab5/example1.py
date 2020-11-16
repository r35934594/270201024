number=int(input("Enter an integer:"))
while number<0:
  print("Please enter a valid number:")
  number=int(input("Enter an integer:"))

for i in range(1,11):
  print(number," x ", i, "=", (number*i))
