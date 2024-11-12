#Dictionary is a type of collection like list
# A list is a collection of items in a sequence
#A dictionary is different
#Dictionaries store data in key-value pairs
#You can retrive data quickly by using a unquie key
#instead of retreving it by index (position)

#Example
#List use brackets, dictionaries use braces
tyreece = {
    "name": "Tyreece",
    "age": 15,
    "city": "St",
    "pets": 2,
    "height": 4.2
}
#Each key must be unique

#Retreiving values from a dictionary

print(tyreece["age"])

#.get allows you to retreive a value without enrroring
#when the key doesn't exisit
#The second parameter is what is give if value is not found
print(tyreece.get("height"))
print(tyreece.get("weight", "Not Found"))
print(tyreece["age"])

#You cna add values to a dictionary
tyreece["country"] = "USA"

#You can modify
tyreece["age"] = 32

print(tyreece)

#Remove entries
#.pop
tyreece.pop("pets")

#Iterate tyhorugh a dictionary using a for loop

for key, value in tyreece.items():


#Dictionary functions
    print(tyreece.keys())   #returns all keys
print(tyreece.values()) #returns all values
print(tyreece.items())  #returns all pairs
print(tyreece.clear())  #removes all items from the dictionary
