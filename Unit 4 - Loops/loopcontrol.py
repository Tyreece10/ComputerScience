##Loop control statments
#Allows you to change how loops operate
#Do things like quit the loop early, skip the current loop, and even do nothing.
#break, continue, and pass

#break
#exit a loop prematurely, before it was supposed to end

#Example

bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruit:

    if fruit == "bug":
        print("Uh oh, you found a bug in the bag...")
        break   #the break statment exits the loop immediately and continues
    else:
        print("You ate a " + fruit)


#Continue
#Skips the current loop
#It does not exit the entire loop, just moves on the the next iteration

#Example
orders = [15, 30, 15, 35, 23, 100, 3, 10, 22]

#Only apply discount for orders above 20 dollars
#Counpon applying program
for order in orders:
    if order < 20:
        continue    #Skips the rest of the loop iteration and goes to the next iteration
    print(str(order) + " discounted 5% to " + str(order * 0.95))


#Pass
#Does nothing
#Usually used as a placehlder while writing code
#TExt adventure project

if True:
    pass

def enter_forest():
    pass

def swim_river():
    pass
def eat_icecream():
    pass