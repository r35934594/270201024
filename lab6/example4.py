#Unique List

item_number=int(input("How many elemens are there in your list? "))

list1=[]
unique_list=[]

for i in range(item_number):
  item=int(input("Please enter your elements: "))
  list1.append(item)

for item in list1:
  if item not in unique_list:
    unique_list.append(item)

unique_list.sort(reverse=True)

print(list1)
print(unique_list)

