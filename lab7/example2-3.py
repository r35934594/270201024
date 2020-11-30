books={"ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"}
book_dict={}
val1,val2,val3=0,0,0
tup=0
for book in books:
  val1=len(book)
  val2=len(set(book))
  val3=int((val1+val2)/2)
  tup=val1,val2,val3
  book_dict.update({book:tup})
print(book_dict)
