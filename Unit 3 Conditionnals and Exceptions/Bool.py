answer = "cube"
count = 1
print(answer == "cube" and count < 10)
pizza = 400
print(pizza == 200)

#Make a 6 question quiz
#1st one is a greater then less then.
#2nd one is a greater then and less then
#Thrid one is a beginning and end
#Fourth one is a how many question one
#Fifth one is a greater than and less then
name = input("Whats your name\n>")
print("Answer theses questions")

answer = int(input("Give me a number greater than 499\n>"))
print(answer > 499)

answer_two = int(input("Give me a number less than 11 but greater 5\n>"))
print(answer_two < 11 and answer_two > 5 )

answer_three = int(input("Give me a number starts with 7 and ends with 5\n>"))
print(answer_three == 75)

answer_four = int(input("How many letters does the word Dad have\n>"))
print(answer_four == 3)

answer_five = int(input("Give me a number greater than 42 but less than 45\n"))
print(answer_five > 42 and answer_five < 45)

print("Well done completing the quiz!!!")