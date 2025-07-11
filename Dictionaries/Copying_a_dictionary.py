# 
# car ={'barnd':'Audi','model':'q7'}
# car_copy = car
# print(id(car))
# print(id(car_copy))
# car_copy['model'] = "q8" '''It will update q8 in both the car and car_copy'''
# print(car)
# print(car_copy)

# Using copy() method
car ={'barnd':'Audi','model':'q7'}
car_copy = car.copy()
print(car_copy)
car_copy['model'] = 'q8'
print(car_copy)
print(car)

# using dict() method

car ={'barnd':'Audi','model':'q7'}
car_copy = dict(car)
print(car_copy)
car_copy['model'] = 'q8'
print(car_copy)
print(car)