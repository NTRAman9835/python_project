# Sanglass pattern of stars
'''Write a program to print Sanglass pattern or of stars as shown:
                * * * * *
                 * * * *
                  * * *
                   * * 
                    *
                    *
                   * *
                  * * * 
                 * * * *
                * * * * * '''
rows = int(input("Enter the row number:"))
for i in range(rows,0,-1):
    for space in range(1,rows-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(' ')
for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(' ')
