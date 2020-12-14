n=5
employee={}
for i in range(n):
  name=input("Please enter a name:")
  salary=input("Please enter a salary:")
  employee[name]=salary
maxsalaries=sorted(employee.values())[-3:]
for person in employee.keys():
  if employee[person] in maxsalaries:
    print(person)
