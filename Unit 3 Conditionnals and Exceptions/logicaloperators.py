#Logical Opeators   =   and, or, !

def check_eligiblity(age, exp):
    #You must be at least 18 year old and have 1 year of experience to be eligible
    if age >= 18 and exp >= 1:
        print("Your are eligible for the competition!")

    elif age < 18:
        print("You are not old enough to compete")

    elif exp < 1:
        print("You don't have enough experience to compete.")

a = int(input("How old are you?\n>"))
e = int(input("How many years of experience do you have?\n>"))

check_eligiblity(a, e)