#!/bin/python3

#Problem 1
def gerat(num1, num2, num3):
    if num1>num2 and num1>num3:
        print(str(num1)+" is greatest")
    elif num2>num1 and num2>num3:
        print(str(num2)+" is greatest")
    else:
        print(str(num3)+" is greatest")

gerat(6, 69, 36)

#Problem 2
def convert(celsius):
    return ((int(celsius) * (9/5))+32)

#c = 45
#fahrenhiet = convert(c)
#print(str(fahrenhiet))
f = convert(45)
print(f)

#Problem 3

def sum(n):
    if n==0 or n==1:
        return 1
    return n + sum(n-1)

print(sum(5))

#Problem 4

n = 3
for i in range(n):
    print("*" * (n-i))

n=3
for i in range(n):
    print("*" * (i+1))
n=3
for i in range (n):
    print(" " * (n-i-1), end='')
    print("*" * (2*i+1), end='')
    print(" " * (n-i-1))
    
#Problem 6
def inch(n):
    return n * 2.54
ko = round(inch(6),2)
print(ko)

#Problem 9
def multable(n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")
multable(6)

