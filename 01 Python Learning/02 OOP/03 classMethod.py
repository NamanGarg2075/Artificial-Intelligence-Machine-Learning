class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def msg(self):
        print(self.name, "got", self.marks,"%")

    @classmethod
    def percentage(cls,name,marks):
        return cls(name,str((marks/600)*100)) # here marks become percentage then msg() calls
    

s1 = Student.percentage("NAMAN", 560) 
s1.msg()