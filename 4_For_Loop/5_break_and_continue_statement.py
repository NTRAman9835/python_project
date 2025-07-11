# Break Statement
# Example-1
# numbers = list(range(0,100))
# for number in numbers:
#     if number>50:
#         break
#     print(number,end=" ")

# Example -> 2
# while True:
#     num = input('Enter the number (q for quit):')
#     if num == 'q':
#         break
#     print(int(num))

# Continue Statement
# Example -> 1
# for i in range(5):
#     if i==2 or i==4:
#         continue
#     print(i)

# Example -> 2
i=1
while i<=10:
    i+=1
    if i%2!=0:
        continue
    print(i,end=" ")