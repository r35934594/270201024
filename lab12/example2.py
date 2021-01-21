class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  
  def set_name(self,name):
    self.name=name
    
  def set_salary(self,salary):
    self.salary=salary

  def get_salary(self):
    return self.salary
class Company:
  def __init__(self,emp_lst=[]):
    self.emp_lst=emp_lst
  
  def set_emp_lst(self,emp_lst):
    self.emp_lst=emp_lst
    
  def get_salary(self):
    print(self.emp_lst)

  def add_emp(self,new_employee):
    if isinstance(new_employee,Employee):
      self.emp_lst.append(new_employee)
  
  def calc_average(self):
    sum=0
    for emp in self.emp_lst:
      sum+=emp.get_salary()
    return sum/len(self.emp_lst)

x=Employee("a",10)
y=Employee("b",20)
z=Company()
z.add_emp(x)
z.add_emp(y)
print(z.calc_average())