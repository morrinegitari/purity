class student :
    def __init__(self,name,gender,age):
        self.name = name
        self.gender =gender
        self.age =age


    def study (self):
        print(self.name,"is studying")

student1 = student("Innocent","male",25)
print(student1.name,student1.gender,student1.age)
student1.study()
student2 = student("abigael","female",18)
student3 = student("abigael","female",18)
student4 = student("abigael","female",18)
student5 = student("abigael","female",18)
