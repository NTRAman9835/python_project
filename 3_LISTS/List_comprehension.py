# Without list comprehension
names=['John','James','Emmy','Michael','Jimmy']
j_names=[]
# for name in names:
#     if ('J' in name):
#         j_names.append(name)
# print(j_names)
# with list comprehension
j_names=[name for name in names if 'J' in name]
print(j_names)