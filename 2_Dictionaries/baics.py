# Dictionaries
car={"Brand":"Audi","model":"q7"}
print(car)
# We can only store one item in one key value
car={"Brand":"Audi","model":"q7",'model':"q8"}
print(car)
# Mutable(Changeable)
car={"Brand":"Audi","model":"q7",'model':"q8"}
car['model']='q9'
print(car)
# Length of dictionary
print(len(car))
# Dict() Constructer
car=dict(brand="Audi",model="q7")
print(car)