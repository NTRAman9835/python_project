'''Write a program of right pyrsmid star
                    *
                    * * 
                    * * * 
                    * * * * 
                    * * * * * 
                    * * * *
                    * * *
                    * * 
                    * '''
rows = int(input("Enter the row number:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()