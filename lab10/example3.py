def sum_of_list(lst,sum=0):
  if lst==[]:
    return sum
  if isinstance(lst[0],list):
    return sum_of_list(lst[0])+sum_of_list(lst[1:],sum)
  sum+=lst[0]
  return sum_of_list(lst[1:],sum)
  

print(sum_of_list([3,12,76,[4,56,43],[2,8],81,75]))

  