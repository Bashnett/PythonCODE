#!/bin/python3

#Problem 1
name = input("Enter Your name")
print("Good Morning",name)

#Problem 2
mail = ''' Dear <|NAME|>,
You are Selected !
<|DATE|>'''
mail = mail.replace("<|NAME|>","Anish")
mail = mail.replace("<|DATE|>","5 November")
print(mail)

# Problem 3
st = "I am a  Hacker"
print(st.find("  "))

#Problem 4
st = st.replace("  "," ")
print(st)

#Problem 5
letter = "Dear anish,\nThis python code is nice.\nThanks\n"
print(letter)
