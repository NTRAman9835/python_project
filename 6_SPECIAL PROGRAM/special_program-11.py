'''Write a program to check whether a 3-digit number is an armstrong number'''
original = int(input("Enter the 3-digit number:"))
number = original
sum=0
if number > 100:
    while number>0:
        digit = number%10
        sum+=digit**3
        number=number//10
    if sum == original:
        print("The {} is armstrong number.".format(original))
    else:
        print("The {} is not armstrong number.".format(original))
else:
    print("Please!! Enter the 3-digit number.")