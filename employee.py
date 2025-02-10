class Employee:
    def __init__(self,name,position,salary):
        self.name =name
        self.position =position
        self.salary =salary

    def info(self):
        print(self.position,"is earning",self.salary)

employee1 = Employee("John","CEO",15000)
print(employee1.name,employee1.position,employee1.salary)
employee1.info()

employee2 = Employee("Luke","Managing Director",16000)
print(employee1.name,employee1.position,employee1.salary)
employee2.info()

employee3 = Employee("Eric","secretary",13000)
print(employee1.name,employee1.position,employee1.salary)
employee3.info()

employee4 = Employee("Evans","IT technician",12000)
print(employee1.name,employee1.position,employee1.salary)
employee4.info()

employee5= Employee("Ian"," Director",15000)
print(employee1.name,employee1.position,employee1.salary)
employee5.info()

employee6 = Employee("Lucy","Manager",26000)
print(employee1.name,employee1.position,employee1.salary)
employee6.info()