def reverse_list(original_list,counter=0):
  for i in original_list:
    if i%2==0:
      counter+=1
  return counter
print(reverse_list([1,2,3,4,6,8,10]))