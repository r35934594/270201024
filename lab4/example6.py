#calculating trailing zeros 
num=int(input("Please enter a number:"))
counter=0  
for i in range(2,num+1):
  while i%5==0:
    counter+=1
    i=i//5
print(counter)    

