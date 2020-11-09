num=int(input("Enter the number:"))
factorial=1
  
if num<0:
  print("Please enter a positive integer!")  
else:  
  for i in range(num):
    factorial*=num
    num-=1

  print(factorial) 
