#!/bin/python

#Problem 1
NepDict= {
        "Kera" : "IT is Banana in Nepali",
        "Mewa" : "It is Papaya in Nepali",
        "Golbheda" : {
            "rato" : "Kalo"}
        "Gulo" : "Dick"
        }
print(NepDict["Kera"])
print(NepDict["Golbheda"]["rato"])
update = {
        "kkalo" : "Black",
        "Rato" : "Red"
        }
NepDict.update(update)
print(NepDict)

# Problem 2
n1 = int(input("Enter first number "))
n2 = int(input("Enter first number "))
n3 = int(input("Enter first number "))
n4 = int(input("Enter first number "))
n5 = int(input("Enter first number "))
n6 = int(input("Enter first number "))

s = {n1, n2, n3, n4, n5, n6}
print(s)

# Problem 6
empDic = {}
a = input("Enter your favourite language")
b = input("enter your favourite language")
c = input("Enter your favourite language")
d = input("Enter your favourite language")
empDic["Anish"] = a
empDic["Manish"] = b
empDic["Ronis"] = c
empDic["Ganesh"] = d
print(empDic)

