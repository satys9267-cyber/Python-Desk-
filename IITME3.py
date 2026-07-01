#Question is create the grade system for students mark with exception handling by using IF else-if ladder


Student_Marks = int(input("Enter the marks of student: "))

if(0<=Student_Marks<=100):
  if(Student_Marks>=90):
    {print("Grade A")}
  elif(90>Student_Marks>=80):
    {print("Grade B")}
  elif(80>Student_Marks>=70):
    {print("Grade C")}
  elif(70>Student_Marks>=60):
    {print("Grade D")}
  elif(60>Student_Marks):
    {print("Grade E")} 
else:
  {print("Invalid Input")}