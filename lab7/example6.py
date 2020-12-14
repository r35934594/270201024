numbers1 = set([2,3,4,20,5,5,15])
numbers2 = set([10,20,20,15,30,40])
intersection=[]
union=[]
for  a in numbers1:
  for b in numbers2:
    if a==b:
      intersection.append([a])
    union.append(b)
  union.append(a)
print(intersection)
print(set(union))

    


