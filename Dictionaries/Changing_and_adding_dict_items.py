# Changing values using key names
car = {'brand':"Audi", 'model':"q7"}
car['model'] = 'q8'
print(car)

# Changing values using update() method
car = {'brand':"Audi", 'model':"q7"}
car.update({'model':'s5'})
print(car)  

# Adding new items using keys names 
car = {'brand':"Audi", 'model':"q7"}
car['Fuel type'] = 'Diesel'
car['color'] = 'Black'
print(car)

# Adding new items usinf update() method
car = {'brand':"Audi", 'model':"q7"}
car.update({'color':'black','fuel type':'Diesel'})
print(car)