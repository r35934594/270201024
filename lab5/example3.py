
number_1=int(input("Enter the first number:"))
number_2=int(input("Enter the second number:"))
counter=0
while number_1>0 or number_2>0:
  if number_1==0 or number_2==0:
    break
  else:
    if number_1%10==number_2%10:
      counter+=1 
      
    number_1=number_1//10
    number_2=number_2//10
      
    print(number_1,number_2,counter)


print(counter)