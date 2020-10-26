GPA=float(input("Please enter your GPA:"))
num_lectures=int(input("Please enter the number of lectures:"))

if GPA<2.0:
  if num_lectures<47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
elif num_lectures<47:
  print("Not enough number of lecturese!")
else:
    print("GRADUATED!")