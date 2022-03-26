#!/bin/python3

# Problem 1
n = int(input("Enter a number"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")


# Problem 2
l1 = ["Harry","Sohan","Sachin","Rahul"]
for i in l1:
    if i.endswith('n'):
        print("Good Morning",i)

# Problem 3
num = int(input("Enter any number"))
i=1
while i<=10:
    print(f"{num}X{i}={num*i}")
    i+=1

# Problem 4-- Type 1
ne = int(input("Enter the number"))
prime = True
for j in range(2, ne):
    if ne%j==0:
        prime = False
        break

if(prime):
    print(str(ne)+" is prime")
else:
        print(str(ne)+" is Composite")

# Problem 4-- Type 2
#nex = int(input("Enter the number"))
#for k in range(1, nex):
#    count=0
#    if nex%k==0:
#        count+=1
#if(count==1):
#    print(str(nex)+" is Prime")
#else:
#    print(str(nex)+" is Composite")

# Problem 5

sett = int(input("Enter the n number"))
z =1
sex=0
while z<=sett:
    sex=sex+z
    z+=1
print(sex)

# Problem 6
mun = int(input("Enter the number"))
fact = 1
for x in range(1, (mun+1)):
    fact = fact*x
print(fact)

# Problem 7 

o =3
for t in range(o):
    print(" " * (o-t-1),end='')
    print("*" * (2*t+1),end='')
    print(" " * (o-t-1))

# Problem 8

for y in range(o):
    print("*" * (y+1))

# Problem 10

net = int(input("Enter the number"))
for s in range(10,1):
    print(f"{net}X{s}={net*s}")

