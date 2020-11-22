password="abc123"
trial=input("Please enter the password:")
while password!=trial:
  if trial=="help":
    print(password[0])
    trial=input("Please enter the password:")
  else:
    trial=input("Wrong,please enter the password:")
print("Welcome")
