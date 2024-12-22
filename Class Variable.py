
# Class Variable
class Student:
    uni_name = "Menoufia National University "
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Salma", "first year")
s2 = Student("Heba", "third year")

print(s1.uni_name) 
print(s2.uni_name) 
print(s1.name) 
print(s2.name) 
print(s1.grade) 
print(s2.grade) 

print(Student.uni_name) 


Student.uni_name = 'menoufia'

print(s1.uni_name) 
print(s2.uni_name) 

