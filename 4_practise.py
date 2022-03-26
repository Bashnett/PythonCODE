#!/bin/python3

#Problem 1 
f1 = input("Enter first fruit name\n")
f2 = input("Enter Second Fruit name\n")
f3 = input("Enter third fruit name\n")
f4 = input("Enter Fourth fruit name\n")
f5 = input("Enter Fifth Fruit name\n")
f6 = input("Enter Sixth Fruit name\n")
fruits = [f1, f2, f3, f4, f5, f6]
print(fruits)

#Problem 2
m1 = int(input("Enter first mark\n"))
m2 = int(input("Enter Second marks\n"))
m3 = int(input("Enter Third marks\n"))
m4 = int(input("Enter fourth marks"))
num=[m1, m2, m3, m4]
num.sort()
print(num)

#Problem 3
tuples=(6, 21, 36, 69)
#tuples[0]= 6 -- It throws error as tuple values cannot be changed
print(tuples)

#Problem 4
u = [1, 30, 2, 3]
print(sum(u))

#Problem 5
a= (7, 0, 8, 0, 0, 9)
print(a.count(0))

