from math import *
from random import *

print(ceil(5.2))

print(dir()) 

#random 

for i in range(10):
  print(randint(1,20))

for i in range(10):
  print(randrange(1,20,2))

list = ["item1", "item2","item3"]
for i in range(10):
  print(choice(list))

#List Comprehensions
#cube inside a list

newList = []
newList = [i**3 for i in range(1, 5)]

'''
for i in range(1,5):
  newList.append(x**2)
'''

print(newList)

#even numbers

newList2 = []
newList2 = [x for x in range(1,20) if x%2 == 0]
print(newList2)

#save the repeated item

lst1 = ["Juan", "Oscar", "Elena", "Robin", "Hood"]
lst2 = ["Robin", "Juan", "Mbappe", "Josh", "Joshua"]

result = []

result = [i for i in lst1 if i in lst2]

print(result)

