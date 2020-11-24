#Identity Matrix

n=int(input("How big is your matrix going to be?"))
lst=[]
counter=0
for i in range(n**2):
  lst.append(0)

for i in range(n**2):
  while counter<(n**2):
    lst[counter]=1
    counter=counter+n+1

print(lst)
