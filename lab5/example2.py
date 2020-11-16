number_count=int(input("How many numbers are there?"))
counts_even=0
for i in range(number_count):
  number=int(input("Enter your number:"))
  if number%2==0:
    counts_even+=1
percentage=counts_even/number_count*100
print("The percentage of even numbers is:",percentage)
