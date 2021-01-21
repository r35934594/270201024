def binary_to_decimal(num,sum=0):
  for i in range(len(num)):
    if num[i]=='1':
      sum=sum+2**int(i)
      print(int(i))
  return sum
print(binary_to_decimal('1111'))