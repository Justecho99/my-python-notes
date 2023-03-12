#// not, and & or
condition1 = True
condition2 = False

not condition1  #False, that's just a negative sth
condition1 and condition2  #False, both gotta be true
condition1 or condition2  #True

#//'or' value//
print(0 or 1)  ## 1
print(False or 'hey')  ## 'hey'
print('hi' or 'hey')  ## 'hi'
print([] or False)  ## 'False'
print(False or [])  ## '[]'; if the first is false then second is true

#//'and' value//
print(0 and 1)  ## 0
print(1 and 0)  ## 0
print(False and 'hey')  ## False
print('hi' and 'hey')  ## 'hey'
print([] and False)  ## []
print(False and [])  ## False

#Bitwise Operators (very, very, rarely used)
"[&] performs binary [and]"
"{|} performs binary {or}"
"[^] performs a binary [xor] operation"
"{~} performs a binary {not} operation"
"[<<] shift left operation"
"{>>} shift right operation"

# Ternany operator
"def is_adult(age):"
"  return True if age > 18 else False"

#Strings
print("beau".upper())
print("BEAU".lower())
print("beaU person".title())
print(" person".islower())

name3 = "Nobo"
print(name3.lower())
print(len(name3))
print("bo" in name3)

#Escaping characters
name4 = 'Be\nau'
print(name4)

#Strings Characters & Slicing
p3 = "Beau is dumb"
print(p3[0:12])
print(p3[:8])
print(p3[5:])
print(p3[1:])

#Booleans
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])

ingredients_purchased = True
meal_cooked = True

ready_to_serve = all([ingredients_purchased, meal_cooked])

#Number Data types
num1 = 2 + 3j
num2 = complex(2, 3)

print(num2.real, num2.imag)

#Built-in functions
print(round(5.5))
print(round(5.49))

#Enums = readable names that are bound to a constat value
from enum import Enum


class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(list(State))
print(len(State))

#User input
age = input("What's your age? ")
print("Your age is " + age)

# Control Statements
condition = True

if condition == True:
  print("The condition was true")
else:
  print("The condition was False")

#Lists
dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

print("Roger" in dogs)

dogs[2] = "Beau"
dogs.append("Bobo") #to add some [objects] to the list
dogs.extend(["Judah", 5]) #to add another [list] to the list
#.extend is like '+='
dogs.remove("Quincy")
print(dogs.pop()) #.pop = remove [the last item on the list] and return an item without it
print(dogs)

ittems = ["Roger", 1, "Syd", True, "Quincy", 7]
ittems.insert(2, "Test") #to add items
ittems[1:1] = ["Test1", "Test2"] #to add multiple items
print(ittems)

#Sorting Lists
stuff = ["Roger", "Syd","Quincy", "Anna", "Bob","beaver"]
print("my stuff is")
#stuff.sort(key=str.lower)#
print(sorted(stuff, key=str.lower))

#Tuples
names = ("Roger", "Syd", "Annie", "Bob")

names[0]
names.index("Roger")

len(names)

print("Roger" in names)
print(sorted(names[:]))

newTuple = names + ("Tina", "GG_man")
print(newTuple)

##Dictionaries

dog = { "name": "Roger", "age": 8}

dog["name"] = "Syd"

print(dog)

cat = { "name": "Roger", "age": 8, "color": "green"}

print(cat.get("name"))
print(cat.popitem())

print("tHeRe It Is:") and print(list(cat.values()))
print("here it is:") and print(list(cat.keys()))
print(len(dog))  and print(list(dog.items()))

del cat['color'] # del = delete

dogCopy = dog.copy()

cat["favorite food"] = "Meat"
print(cat)


#'is' & 'in' operators

# (1 + 1 = 2, 2 - 1 = 1, 2 * 2 = 4, 4 / 2 = 2, 4 % 3 = 1, 4 ** 2 = 16, 4 // 2 = 2)
