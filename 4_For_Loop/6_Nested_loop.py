# Nested for loop

list1 = [1,2,3]
list2 = [4,5,6]

for i in list1:
    for j in list2:
        print(i, j)
    print()

# Nested while loop
i=0
j=0
while i < len(list1):
    while j < len(list2):
        print(list1[i], list2[j])
        j+=1
    print()
    i+=1