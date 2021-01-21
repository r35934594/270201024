def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return "not prime"
  return "prime"

def print_primes_between(x,y):
  for num in range(x,y+1):
    if num>1:
      if is_prime(num)=="prime":
        print(num)

x=int(input("Enter an integer:"))
y=int(input("Enter an integer:"))
print_primes_between(x,y)
