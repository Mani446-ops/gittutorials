
age = 20

if age>18:
    print("He can vote")

number = 10

if number>0:
    print("Positive number")

age=16

if age>=18:
    print("He can vote")
else:
    print("He cannot vote")

number=11

if number % 2==0:
    print("Even number")
else:
    print("Odd number")

marks=67

if marks>90:
    print("Excellent")
elif marks>80:
    print("Distintion")
elif marks>70:
    print("Good")
else:
    print("Fail")

age=67
salary=8000

if age>39 and salary>12000:
    print("Loan approved")
else:
    print("Loan not approved")

age=28
has_id=True

if age>18:
    if has_id:
        print("Allowed")
    else:
        print("Required ID")
else:
    print("Underage")

a=34
b=46
c=67

if a>b and a>c:
    print("Largest:",a)
elif b>c:
    print("Largest:",b)
else:
    print("Largest:",c)

number=8

if number>0:
    print("Positive")
elif number==0:
    print("Zero")
else:
    print("Negative")
