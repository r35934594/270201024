a_list=[12,-7,5,-89.4,3,27,56,57.3]

def find_sum(lst,sum=0):
  for i in lst:
    sum+=i
  return sum
print(find_sum(a_list)) 