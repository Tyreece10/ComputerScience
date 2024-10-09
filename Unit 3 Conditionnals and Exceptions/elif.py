x = 5

if x > 0:   #
    print("x is a positive number")
#Have to be together

elif x < 0:   #elif statement are always paired to an if
    print("x is a negative number!")


else:   #else statement are always paired to an if statment/ else statment never takes a condition
    print("x is a negative number!")

color = "red"

color = input("What color is the light\n>")

if color.lower() == "green":        #Only 1
    print("GO")

elif color.lower() == "yellow":     #As many
    print("Stop")

elif color.lower() == "yellow":
    print("STOP IF SAFE")
 
else:   #Only 1
    print("stop if you can")




x = 10

if x > 5:
    print("x is greater than five")

if x > 8:
    print("x is greater than eight")

if x > 5:
    print("x is greater than five")

elif x > 8:
    print("x is greater than eight")