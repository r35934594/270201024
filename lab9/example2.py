def reverse_list(original_list):
  new_list=[]
  for i in original_list[::-1]:
    new_list.append(i)
  return new_list
print(reverse_list([1,2,3,4]))