month=int(input("Please enter the month:"))
day=int(input("Please enter the day:"))

if month>=3 and month<=5:
  if month==3 and day<20:
    print("Winter")
  else: 
    print("Spring")
elif month>=6 and month<=8:
  if month==6 and day<21:
    print("Spring")
  else:
    print("Summer"+"1")
elif month>=9 and month<=11:
  if month==9 and day<22:
    print("Summer"+"2")
  else:
    print("Fall")
elif month==12 and day<21:
  print("Fall")
else:
    print("Winter")