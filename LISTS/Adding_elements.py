# Adding elements using append method
lanuages=['c','java','html']
lanuages.append(input("Enter adding element:"))
# /Adding a list in list
lanuages.append(["python","c++"])
print(lanuages)
print("\n")
# Adding items using insert method
lanuages1=['c','java','c++']
lanuages1.insert(0,"python")
print(lanuages1)
#  Adding items using extend() method
lanuages.extend(lanuages1)
print(lanuages)