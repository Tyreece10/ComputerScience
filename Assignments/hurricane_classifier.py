wind_speed = int(input("What is the wind speed of your hurricane?\n>"))
if wind_speed < 74:
    print("Your hurricane is a Tropical Storm")

elif wind_speed < 96:
    print("Your hurricane is a Catagory 1")

elif wind_speed < 111:
    print("Your hurricane is a Catagory 2")

elif wind_speed < 130:
    print("Your hurricane is a Catagory 3")

elif wind_speed < 157:
    print("Your hurricane is a Catagory 4")

elif wind_speed >= 157:
    print("Your hurricane is a Catagory 5")