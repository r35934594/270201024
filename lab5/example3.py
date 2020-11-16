number_1=input("Enter the first number:")
number_2=input("Enter the second number:")
counter=0
for char_1 in number_1:
  for char_2 in number_2:
    if char_1==char_2:
      counter+=1
print("Matching number of digits is:",counter)