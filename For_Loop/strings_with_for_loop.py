# Acessing all the characters using for loop

name = 'Aman'
for c in name:
    print(c,end=" ")
print()

name = 'Aman'
for c in name[::-1]:
    print(c,end=" ")
print()

names = 'Aman Rahul Manish Soyam'
count = 0
for name in names.split():
    count+=1
print(f"There are {count} in names")