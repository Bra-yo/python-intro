courses = ["MIT","Cyber security","Data Science"]

#Accessing an element fromana array through index position
print(courses[1])


#looping through an array
for y in courses :
    print("Course is",y)

#Adding a new element into an array
courses.append("Laravel")
for v in courses :
    print(v,"is an updated course")

#deleting an element
courses.remove("MIT")
print(courses)