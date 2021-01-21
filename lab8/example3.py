import random

def rand_int(a,b,n):
  return random.sample(range(a,b),n)
def get_overlap(list1,list2):
  list3=[]
  for i in list1:
    for x in list2:
      if i==x:
        list3.append(x)
  print(list1,list2)
  return list3
print(get_overlap(rand_int(0,10,5),rand_int(0,10,5)))
