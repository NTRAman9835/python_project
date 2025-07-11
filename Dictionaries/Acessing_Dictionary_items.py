# Acessing Values using key names
car={"Brand":"Audi","model":"q7"}
print(car["Brand"])

# Acessing values using get() method
car = {'Brand':'Audi', 'model':'q7'}
print(car.get("model"))

# Acessing keys using key() method
car = {'Brand':'Audi', 'model':'q7'}
car_keys = car.keys()
car['Fuel type'] = "Diesel"
print(car_keys)

# Acessimg values using values() method
car = {'Brand':'Audi', 'model':'q7'}
car_values = car.values()
print(car_values)
car['Fuel type'] = 'Diesel'
print(car_values)

# Acessing items using items() method 
car = {'Brand':'Audi', 'model':'q7'}
car_items = car.items()
print(car_items)
car['Fuel type'] = 'Diesel'
print(car_items)
