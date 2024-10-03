#functions
print("Hello, World!")      # "Hello, World!" is the parameter
input("Please enter your username\n>")      #\n is an escape character
                                    # \n starts a new line (linebreakers)
#Some conversion fuctions
# input is never required

#variables
#Syntax
# <name> = <value>
x = 5    # x is name and 5 is value   

#Snake naming convention - lowercase then underscore for spaces
#CONCISE: Short and descriptive

username = "osowski"        #Define string
fav_animal = "Calugo"       #Define string
total_poptarts = 12         #Define integer (Whole number)
percent_complete = 23.52    #Define float (demcial number)
is_cool = True              #Define Boolean (True/False)
first_leater = 'c'          #Define Character (single symbol)

total_poptarts = 8      #ressign - changes the value

#Arithmetic Operators
# + -   *   /   **  %   //
print(4 + 4)    #>8
print("4" + "4") #> 44
print("cat" + "dog") #>catdog
print("cat" * 3)    #> catcatcat
print("cat" + 3)        #> ERROR: Cannot use + for string and int

#Make some working programs
#1. add two numbers
x = int(input("What is x?\n>"))     #input resturns as a string
x = int(x)
y = int(input("What is y?\n>"))     #even if you type in a nmber
y = int(y)
print(str(x + y))

#2. Converts celcius to farenheight
temp_celcuis = input("What is the temperature in Celcius?\n>")
temp_farenheight = int(temp_celcuis * 1.8) + 32
print(temp_celcuis + "degrees C equals " + temp_farenheight + " degrees F")



#Some conversion functions
str()
int()
float()
bin()
bool()

#The stuff that goes between the parenthesis is called PARAMETERS
#Parameters are the values that function needs to run


#Functions
#Functions are like variables
#They have names
#They can be recalled from memory by calling hier name
#They Store information
#Variable store values, functions store code
def potato(): # def keyword + name + () + :
    print("potato")     #lines indented are "inside" functions

#functions are not ran when they are defined
#must be called by name to run
potato()
        # Every function called need parenthesis
        #even if it has no parameters

def jump(how_high):
    print("You jumpped " + str(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("Z", "a", "c", "k", "O", "s", "o", "w", "s", "k", "i")

#Functions can have many lines
def yop_ten_games():
    print("1. Elden Ring")
    print("2. Shadow of the Colossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Gran Turismo 7")
    print("6. Overwatch")
    print("7. Rachet & Clank: Up Your Arsenal")

#Scope: Gloabal and Local Variables!
#Scope refers to the context in which the variable was defined
#GLOBAL - defined at no indentation level
#LOCAL - defined inside of a function

#Global variables can be used anywhere
todd = "cool guy"       #Global variable - no indentation level

#Local variables only exist in the scope they were defined
def my_function():
    smith = "not cool guy"      #Local variable - define i a function
    tood = "strange guy"        #Local variable even though it has same name
    print(todd)     #Prints the local variable todd
    #When you call a variable in a function
    #it seraches local variable first, then global variables

#If you want to ressign a global variable inside of a function
todd = "cool guy"
def my_function2():
    global todd             #In this function, when I call todd
#I mean the global todd, not local
    todd = "strange  guy"   #Reassign todd - global
    print(todd)             #print todd - global

#Return functions
#function =s can also return values
#The value that is returned is sent back to where the function was called
#This is similar to how a variable works
#The function does its work and returns an answer back
def add2(x, y):
    return x + y        #returns the sum of x and y the where the function was called

add2(2, 10)      #Does not print anything! never told to print

answer = add2