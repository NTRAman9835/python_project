age=32
nationality="Indian"
if age>18 and age<30 and nationality=="Indian":
    print("You'r eligible for this Exam")
else:
    print("You are not eligible for this Exam")
age=25
nationality="American"
if age>18 and age<30 and nationality=="Indian":
    print("You'r eligible for this Exam and Exam Fee is ₹1500")
elif age>18 and age<30 and nationality=="American":
    print("You are not eligible for this Exam and Exam fee is $50")
else:
    print("You are not eligible for this Exam")