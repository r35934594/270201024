number=int(input("Enter your number:"))
last_digit=(number%10)
second_last_digit=((number%100)-last_digit)/10
if number<10:
  second_last_digit=0
print(last_digit+second_last_digit)