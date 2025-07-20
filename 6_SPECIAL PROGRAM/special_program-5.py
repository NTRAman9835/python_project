'''Write a program to print the full pyramid sof stars as shown :
                     *
                    * *
                    * * *
                    * * * *
                    * * * * *'''
rows = int(input("Enter the rows number:"))
for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')