'''Write a program to print Diamond shape star 
                *
               * * 
              * * *
             * * * *
            * * * * *
             * * * *
              * * *
               * *
                *'''
rows = int(input("Enter te number of rows:"))
for i in range(1,rows+1):
    for space in range (1,rows-i+1):
        print(" ",end="")
    for star in range(1,i+1):
        print("*",end=" ")
    print(' ')
for i in range(rows-1,0,-1):
    for space in range (1,rows-i+1):
        print(" ",end="")
    for star in range(1,i+1):
        print("*",end=" ")
    print(' ')
