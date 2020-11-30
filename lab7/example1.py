person=dict({("Jon",15),("Ned",45),("Arya",9),("Catelyn",44),("Bran",18)})

for i in person:
  name=person.keys()
  if person[i]>18:
    print(i)
print(name)