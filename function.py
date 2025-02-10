#Built-in function/standard library function

y = max(45,89,75,63,45,14,25)
print("The maximum value is",y)

x = min(25,54,69,12,56,47)
print("the minimum value is", x)

#user-defined functions
def school ():
    print("emobilis")

school()

def add ():
    num1 =5
    num2 =3
    print(num1+num2)

add()

#parameter/variable and argument/value
def multiply (a , b) :
    print(a*b)
multiply(2,5)
multiply(4,8)

def employee (name,age,gender,salary,position):
    print(name,age,gender,salary,position)
employee("Morrine",25,"female",560000,"CEO")
employee("Eric",28,"male",60000,"managing director")
employee("John",27,"male",80000,"technician")
employee("Mary",35,"female",60000,"manager")
employee("Sarah",55,"female",62000,"team leader")


#A program to display details of 5 patients in a hospital
#using a user defined function implement parameters and argument
# fullname,gender,age,disease

def patient (name,gender,age,disease):
    print(name,gender,age,disease)
patient("mary melvis","female",24,"malaria")
patient("Blessing mwangi","female",26,"Pneumonia")
patient("Steve Eric","male",32,"measles")
patient("Purity gitari","female",29,"HIV/AIDS")
patient("Susan Mary","female",28,"Influenza")


