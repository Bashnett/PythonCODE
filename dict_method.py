#!/usr/bin/python
myDict = {
	"Fast" : "In a Quick Manner",
	"Harry" : "A Coder",
	"Marks" : [1, 2, 5],
	"anotherdict" : {'harry':'Player'},
	1: 2
}

print(list(myDict.keys())) # prints the keys of the dictionary in list
print(myDict.values())     # Prints the values of dictionary
print(myDict.items())      # Prints the (key, values) of dictionary
print(myDict)
updateDict = {
"Lovish": "Friend"
}
myDict.update(updateDict)
print(myDict)
