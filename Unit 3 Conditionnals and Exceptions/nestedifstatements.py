#Nested if statements
#You are a Prime member OR order is at least $25
#You are at least 18 year old OR have parent consent

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("You are eligible for free shipping!")
    if consent:
        print("You are not eligible for free shipping! ")

elif cost >= 25:
    if age >= 18:
        print("You are eligible for free shipping!")
    elif consent:
        print("You are eligible for free shipping!")
    else:
        print("You are NOT eligible for free shipping!")

else:
    print("You are Not eligible for free shipping!")


#Do we need an umbrella?

#We need an umbrella if it is raining and we are outside.

raining = True
outside = True

if raining and outside:
    print("Bring and umbrella")

else:
    print("don't bring an umbrella")



if raining:
    if outside:
        print("Bring an umbrella")
    else:
        print("Don't bring an umbrella.")



raining = input("Is it raining todat?")

if raining.lower() == "yes":
    outside = input('Are you going outside today?')

    if outside.lower() == 'yes':
        print('Bring an umbrella')
    else:
        print("Don't bring an umbrella")