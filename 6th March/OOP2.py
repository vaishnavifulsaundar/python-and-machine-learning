class Student:
    School = "Abhinav"                              # Class variable
    
    def __init__(self,no1,no2,no3):
        self.m1 = no1                                 # Instance Variable
        self.m2 = no2
        self.m3 = no3
        
    def Instance_Total(self):                       # Instance method
        print("Inside instance method")
        return self.m1 + self.m2 + self.m3
        
    @classmethod                                     # Decorator
    def Class_DisplaySchool(cls):               # class method
        print("School name is :",cls.School)
        
    @staticmethod                                   # Decorator
    def Static_Info():                                 # Static method
        print("This class contains the information of school")

def main():
    Student.Class_DisplaySchool()           # Calling class method
    obj1 = Student(50,80,70)                    # object creation
    obj2 = Student(65,80,75)
    ret = obj1.Instance_Total()                 # Callling insrtance method
    print("Total obtained marks", ret)
    Student.Static_Info()                          # Calling static method
    
if __name__ == "__main__":                  # App starter
    main()

