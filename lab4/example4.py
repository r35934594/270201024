a=int(input("Enter the base number:"))
b=int(input("Enter the power:"))
result=1

if (a==0 and b==0) or b<0:
  print("Expression is not defined!")
else:  
  for i in range(b):
    result*=a
  print(result)