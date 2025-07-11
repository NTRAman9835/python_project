# f_string
name="Aman"
city="Sultanganj"
age=19
gender='male'
print(f"My Name is {name} and i live in {city}")
# Call to methods
print(f'My name is {name.upper()} and i live in {city.upper()}')
print(f'My name is {name.lower()} and i live in {city.lower()}')
# Multiline f_string
introduction=(f'My name is {name}.'\
              f'My Age is {age}'\
                f'and I am {gender}')
myself=(f'My name is {name}.'
              f'My Age is {age}.'
                f'and I am {gender}.')             
print(introduction)
print(myself)
# Quotation Mark
print('{"Aman"}')
print("{'Aman'}")
print('''Aman''')
#Curlu Braces
x=20
y=10
print(f"The result of x+y is {x+y}")