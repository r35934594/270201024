#Trace of a matrix
n=int(input("How big is your matrix going to be?"))
lst=[]
counter=0
sum=0

for i in range(n**2):
  num=int(input("Enter your number here:"))
  lst.append(num)

for i in range(n**2):
  while counter<(n**2):
    sum=sum+lst[counter]
    counter=counter+n+1
    
print(lst)
print(sum)