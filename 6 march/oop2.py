class Student:
 School = "abhinav"                             #class variable
 
 def __init__(self,no1,no2,no3):
  self.m1 = no1                              #instance variable
  self.m2 = no2  
  self.m3 = no3    
 
 def Instance_Total(self):                  #instance method
  print("inside instance method")
  return self.m1 + self.m2 + self.m3
  
 @classmethod                               #decorator
 def Class_DispalySchool(cls):             #class method
  print("school name is:",cls.School)

  
 @staticmethod                           #decorator
 def static_info():                       #static method
  print("this class contains the information of school")
  
  
def main():
 Student.Class_DisplaySchool()        #calling class method
 obj1 = Student(50,80,70)               #object creation
 obj2 = Student(65,80,75)
 ret = obj1.Instance_Total()
 print("total obtained marks",ret)
 Student.static_info()

if __name__== "__main__":
 main()