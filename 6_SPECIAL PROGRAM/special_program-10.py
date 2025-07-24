'''Write a program to check whether a given 3-digit number is palidrome number'''
original = int(input("Enter the 3-digit number:"))
if original>=100:
    number = original
    digit = 0
    temp = 0
    while number!=0:
        digit = number % 10
        temp = temp*10+digit
        number = number//10
    if temp == original:
        print("The {} is palindrome".format(original))
    else:
        print("The {} is not palidrome".format(original))
else:
    print("Please!! Enter the three digit number.")