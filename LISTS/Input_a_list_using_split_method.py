# Create a list of numbers 67,80,95,5
n=int(input("Enter the number of elements:"))
numbers=input("Enter the numbers:").split()
for i in range(0,n):
    numbers[i]=int(numbers[i])
print(numbers)