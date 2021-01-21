lst=[]
def hailstone(x):
  lst.append(int(x))
  if x==1:
    return print(lst)
  if x%2==0:
    return hailstone(x/2)
  if x%2!=0:
    return hailstone(3*x+1)
 
hailstone(11)
