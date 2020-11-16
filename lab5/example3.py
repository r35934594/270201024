number_1=int(input("Enter the first number:"))
while number_1<0:
  number_1=int(input("Please enter a valid number:"))
number_2=int(input("Enter the second number:"))
while number_2<0:
  number_2=input("Please enter a valid number:")
counter=0
number_1=str(number_1)
number_2=str(number_2)

for char_1 in number_1:
  for char_2 in number_2:
    if char_1==char_2:
      counter+=1
print("Matching number of digits is:",counter)

#n1=int(input("N1:"))
#n2=int(input("N2:"))
#match=0
#while n>0 and while n>2:
# if n1%10=n2%10:
#   match+=1
#  n1=n1//10
#  n2=n2//10
#print(match)