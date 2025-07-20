'''Write a program to print multiplication table pattern shown as:
                    1
                    2 4
                    3 6 9 
                    4 8 12 16
                    5 10 15 20 25'''
rows = int(input("Enter the rows number:"))
for i in range (1,rows+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()