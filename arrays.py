courses =["MIT","Cybersecurity","datascience"]
print(courses)
# accessing an element
print(courses[2])

#looping through an array
for x in courses :
    print("course is",x)

 #adding a new element into an array
courses.append("laravel")
print(courses)
# removing an element in an array
courses.remove("Cybersecurity")
print(courses)
