counter=int(input("How many fibonacci numbers should be dısplayed?"))
total=0
num_1=1
num_2=1

for i in range(1,counter+1):
  print(num_1)
  total=num_1+num_2
  num_1=num_2
  num_2=total
