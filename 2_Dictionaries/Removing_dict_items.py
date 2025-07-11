# Removing items using pop() method 
# car ={'barnd':'Audi','model':'q7'}
# print(car.pop('model'))
# print(car)

# Removing an item using popitem() method
car ={'barnd':'Audi','model':'q7'}
print(car.popitem())
print(car)

# Removing an item using del keyword
car ={'barnd':'Audi','model':'q7'}
del car['model']
print(car)

# Removing a dictionary using del keyword
car ={'barnd':'Audi','model':'q7'}
del car

# Empty a dictionary using clear() method
car ={'barnd':'Audi','model':'q7'}
car.clear()
print(car)