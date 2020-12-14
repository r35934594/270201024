#Identity Matrix

n=int(input("How big is your matrix going to be?"))
matrix=[]
lst=[]
counter=0

for i in range(n):
  lst=[0]*n
  lst[i]=1
  matrix.append(lst)

print(matrix)
