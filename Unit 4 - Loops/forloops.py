#For Loops
#This is important
#For loops allows the programmer to REPEAT, OR  WHAT WE CALL LOOP

#Write a program that prints the number 1 through 10

#for <temp var> in <list>:


for i in range(0, 10):        #lines inside of the for loops/it takes a list and goes through the list til it goes through every item in the list.
    print(i)        # i start out as 0


top_foods = ["Eggs", "Chicken", "Mac and Cheese"]
#Go through every food in top_food
#Repeats everything in the for ;oop for each item in the list
#Where food equals the current item
for food in top_foods:      #i and food are temp variables
    print(food)

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#PRACTICE: Create a list of groceries - 
#Contains milk, eggs, bread, butter, and apples
#Ask for user input and an item they purchased
#If the item was on the list, print ("<item> crossed off the list!")
#Remove that item from the list
#You will need to use a for loop to search for that item
#You will need an if statement in the for loop to check

groceries = ["milk", "eggs", "bread", "butter", "apples"]


purchased_item = input("What items have you purchased?\n>")

for grocery in groceries:
    if grocery == purchased_item.lower:
        print(grocery + " checked off the list!")
        groceries.remove(grocery)

print(groceries)

#Create a list of five random numbers from 0-100
#Use a for loops to find the sum of those numbers

import random
numbers = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

for nums in numbers:
    total_sum = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])
    print("Total sum:", total_sum )