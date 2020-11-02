a=float(input("Please enter the parameter of x^2:"))
b=float(input("Please enter the parameter of x:"))
c=float(input("Please enter the parameter of the constant:"))

discriminant=(b**2)+(-4*a*c)

if discriminant>0:
  x_1=(-b+(discriminant)**(1/2))/(2*a)
  x_2=(-b-(discriminant)**(1/2))/(2*a)
  print("First x value is ", x_1 ,"and the second value is ",x_2)
elif discriminant==0:
  x=-b/(2*a)
  print("x s ",x)
else:
  x_1=-b/(2*a)
  i_1=((-discriminant)**(1/2))/(2*a)
  x_2=-b/(2*a)
  i_2=-((-discriminant)**(1/2))/(2*a)
  print("First x value is ",x_1,"+",i_1
,"i","and the second value is ",x_2, "+",i_2,"i")
  
