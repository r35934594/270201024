students=int(input("How many students are there?"))
grades=[]
final_grades=[]
for i in range(students):
  midterm1=int(input("Please enter the student's first midterm:"))
    
  midterm2=int(input("Please enter the student's second midterm:"))
  
  final=int(input("Please enter the student's final:"))
   
  weigthed_grade=midterm1*0.3+midterm2*0.3+final*0.4
 
  grades.append([midterm1,midterm2,final])
  final_grades.append([weigthed_grade])

print(grades)
print(final_grades)


