# Iteration over a dictionary
course = {"name": "python" , "instructor": "Jaspreet" }
for x in course:
    print(x)

# Acessing values of a dictionary
course = {"name": "python" , "instructor": "Jaspreet" }
for x in course:
    print(course[x])
# Acessing values of a dictionary using values() method
course = {"name": "python" , "instructor": "Jaspreet" }
for y in course.values():
    print(y)
# Accessing keys of a dictionary
course = {"name": "python" , "instructor": "Jaspreet" }
for y in course.keys():
    print(y)
# Accessing keys and values of a dictionary
course = {"name": "python" , "instructor": "Jaspreet" }
for x,y in course.items():
    print(x,y)