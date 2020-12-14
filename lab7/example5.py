password=input("Enter your password:")
countupper=0
countlower=0
countnum=0
for char in password:
  if char.isnumeric():
    countnum=countnum+1
  else:
    if char>char.upper():
      countlower=countlower+1
    if char<char.lower():
      countupper=countupper+1
if  countlower<1 or countupper<1or countnum<1:
  print("Sorry it's not valid.")
  


