def selection_sort(lst):
  for bottom in range(len(lst)-1):
    temp=bottom
    for i in range(bottom+1,len(lst)):
      if lst[i]<lst[temp]:
        temp=i
    lst[bottom],lst[temp]=lst[temp],lst[bottom] 
  print(lst)

selection_sort([22,8,12,-4,27,30,36,50,7,68,91,56,2,85,42,98,25])