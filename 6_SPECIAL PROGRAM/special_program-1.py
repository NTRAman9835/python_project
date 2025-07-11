'''Write a program to separate even and odd numbers started a list in two different lists'''

li = list(range(1,25))
evenNumbers = []
oddNumbers = []
for item in li:
    if item%2 == 0:
        evenNumbers.append(item)
    else:
        oddNumbers.append(item)
print(evenNumbers)
print(oddNumbers)