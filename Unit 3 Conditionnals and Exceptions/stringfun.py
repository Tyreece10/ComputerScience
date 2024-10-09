#String functions1
# group of like-functions that manipulate strings
#Modify strings
#Super easy and convenient to use


#   .Lower()
# convers a string to all lowercase
#no matter what the input casing is, its converted to lowercase
#answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)


#.upper()
#Converts a string to uppercase!
x = "hello world".upper()
print(x)

#.capitalize()
#converts to lowervase, then capitalizes the first letter
y = "HelLow WorLd".capitalize()
print(y)    #print "Hello world"

#.title()
#converts a string to titlecase
#capital fisrt letter of words
z = "HelLo woRLd".title()
print(z)

#.swapcase()
#inverts the casing of each character
q = "Hello World!".swapcase()
print(q)    #print "hEllO WOrld"