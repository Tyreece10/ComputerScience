#Iv statement evaluate boolean  expressions
#Make descisions about which code to run

#Take a temperature
#Print "<temperature> is hot" if the temperature is >= 80
#Otherwise print "<temperature> is not hot"
temperature = input("What is the temperature?\n>")
temperature = int(temperature)
#if, boolean expression, :
#sort of like a function, n parenthesis
if temperature >= 80:
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is hot")
    
else:   #Else takes NO condition and runs when the if above is false
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is not hot")








real_password = "skibidi68"
input_password = input("Please enter the password\n>")

if input_password == real_password:
    print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")

    #2
#Create a five question quiz that prints your score at the end
#Any five question

name = input("Whats your name?\n>")
print("Answer these questions")

answer = int(input("Give me a number greater than 499\n>"))
print(answer > 499)
if answer > 499:
    print(answer + 1)

answer_two = int(input("Give me a number less than 11 but greater 5\n>"))
print(answer_two < 11 and answer_two > 5)
if answer_two < 11 and answer_two > 5:
    print(answer_two + 1)

answer_three = int(input("Give me a number starts with 7 and ends with 5\n>"))
print(answer_three == 75)
if answer_three == 75:
    print(answer_three + 1)

answer_four = int(input("How many letters does the word Dad have\n>"))
print(answer_four == 3)


answer_five = int(input("Give me a number greater than 42 but less than 45\n"))
print(answer_five > 42 and answer_five < 45)


score = 2


if answer and answer_two and answer_three and answer_four and answer_five == correct:
    print(5/5)
