#There are a couple types of loops in python
#The for loop lets your iterate list
#-great for looping a set of numbers of times
#BUT WHAT IF we need to loop to an uncertian number of times?
# ex. Entering your password.
#You could get it right the first time
#IT could take you a million tries
#Or anything in between

real_pass = "potato45"
entered_pass = ""
attempts = 0
count = 0

# A While loops continues looping until the condition is no longer True.
while real_pass != entered_pass:        #Check if the entered password matches the real one/Continue looping till it matches real_pass
    #ask for pass
    entered_pass = input("Please enter the password\n>")

    #Check if the password correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
        print(f"Your have tried {attempts} times.")
    else:
        print("ACCESS DENIED")
        print("Try again...")
        attempts += 1

#End password word checking
print("Welcome!")


#Try this
#UPDATE this while loop so it prints how many attempys you are on
#Print number of attempts every loops




#With while loops, be careful for inf loops
#When you put your computer in rest mode, it has nightmare about inf loops /joke
#An inf loop happens when you enter a while loop that can never be escaped.
# ex. (do not click run...)

while count < 10:
    count += 1
    print(count)


#Real word Example:
#"Type "exit" to quit

user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print("Your entered: " + user_input)

print("All done")