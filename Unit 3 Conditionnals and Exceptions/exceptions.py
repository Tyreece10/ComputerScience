#Exception Handling
#Write a program that ask for two numbers and adds them

#if = try
#elif = except speific error type
#else = except
def divide_two_numbers():
    try:
        x = int(input("What the first number?\n>"))
        y = int(input("Whats the second number?\n>"))
        print(x / y)

    except ValueError:                          #Labels the error
        print("Please enter a number....")
        divide_two_numbers()

    except ZeroDivisionError:
        print("Cannot divide by zero...")
        divide_two_numbers()


    finally:
        print()


divide_two_numbers()