# Python has four types of collections
# Tuple
#Set
#List
# Dictionary

#Were going to focus on lists
#A list is a way to store more than 1 value in a single variable
#Those calue in the list are called ITEMS
#ITEMS can be accesed by their index (positionin the list)
#INDEX                           0                1                2              3                 4
best_elden_ring_weaps = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]       #strings

#INDEX         0      1     2     3
best_years = [1776, 1985, 1994, 1957]       #int

#best
print(best_elden_ring_weaps[0])

#List items can be changed
best_elden_ring_weaps[3] = "Spiked Fist"
print(best_elden_ring_weaps)


#Remove the last item in the list by its position in the list = .pop
best_elden_ring_weaps.pop(4)
print(best_elden_ring_weaps)


#Remove an item by its value
best_elden_ring_weaps.remove("Moonveil")
print(best_elden_ring_weaps)

#Add new item to the end of a list
best_elden_ring_weaps.append("Mogwyn's Sacred Spear")
print(best_elden_ring_weaps)


import random
numbers = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
print(numbers)
print(max(numbers))         #max = highest
print(min(numbers))         #min = lowest
numbers.sort()              #low to high
print(numbers)




#worst of the best
print(best_elden_ring_weaps[3])

print(len(best_elden_ring_weaps))

print(best_elden_ring_weaps[len(best_elden_ring_weaps)-1])

#Strings are lists!
#Strings are just a lists of characters
word = "potato"
print(word[0])


#print the index of the value in the list
print(best_years.index(1985))           #.index = index number