def multiplication(n,counter=3):
  if counter==1:
    return n
  counter=counter-1
  return n+multiplication(n,counter)
print(multiplication(1))