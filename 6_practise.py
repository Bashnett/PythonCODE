#!/bin/python3

# Problem 1
a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
d = int(input("Enter Number"))
if a>b:
    f1 = a
else:
    f1 = b
if c>d:
    f2 = c
else:
    f2 = d
if f1>f2:
    print(str(f1) + " is Greatest")
else:
    print(str(f2) + " is Greatest")


# Problem 2
math = int(input("Enter math marks"))
C = int(input("Enter C marks"))
Python = int(input("Enter Python marks"))
total = ((math + C + Python)/300)*100
if math<33 and C<33 and Python<33:
    print("You are failed because you have got less than 33 in one s=Subject")
elif total>=40:
    print("He is passed with more than 40")
else:
    print("He is Failed")

#Problem 3
text = input("Enter your message")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("It is Spam")
else:
    print("It is Not")

# Problem 4
name = input("Enter your username")
a = len(name)
if a>10:
    print("This username is Valid")
else:
    print("Username must be more than 10 letters")


# Problem 5
names = ["Harry","Shyam","Ram","Somesh"]
name = input("Enter the name")
if name in names:
    print(name+" is present in names")
else:
    print(name+" is not present in names")

#Problem 6
marks = int(input("Enter the marks"))
if marks>90 and marks<=100:
    print("Your Result is Excellence")
elif marks>80 and marks<=90:
    print("A")
if marks>70 and marks<=80:
    print("B")
if marks>=60 and marks<=70:
    print("C")
if marks>=50 and marks<=60:
    print("D")
else:
    print("F off")
    
#marks = int(input("Enter Your Marks\n"))

#if marks>=90:
#    grade = "Ex"
#elif marks>=80:
#    grade = "A"
#elif marks>=70:
#    grade = "B"
#elif marks>=60:
#    grade = "C"
#elif marks>=50:
#    grade = "D" 
#else:
#    grade = "F"



print("Your grade is " + grade)  
