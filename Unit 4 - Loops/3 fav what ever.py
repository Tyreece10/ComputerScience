fav_thing = input("Whats your 1st favorite thing\n>")
fav_thing1 = input("Whats your 2nd favorite thing\n>")
fav_thing2 = input("Whats your 3rd favorite thing\n>")
fav_thing3 = input("Whats your 4th favorite thing\n>")
#                   0         1         2           3
fav_things = [fav_thing, fav_thing1, fav_thing2, fav_thing3]


print(fav_things)

print(len(fav_things))


print(fav_things[len(fav_things)-1])




#Create a program that asks for three fav things and puts them in a list


#Real one
top_foods = []

top_foods.append(input("What is your favorite food?\n>"))
top_foods.append(input("What is your favorite food?\n>"))
top_foods.append(input("What is your favorite food?\n>"))


print(top_foods)