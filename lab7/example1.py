tup=[("Jon",15),("Ned",45),("Arya",9),("Catelyn",44),("Bran",18)]
dic= {} 
for person in tup:
  dic[person[0]]=person[1]
  if person[1]>18:
    print(person[0])

