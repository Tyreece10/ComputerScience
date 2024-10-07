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

answer_2 = int(input("Give me a number less than 11 but greater 5\n>"))
print(answer_2 < 11 and answer_2 > 5 )

answer_3 = int(input("Give me a number starts with 7 and ends with 5\n>"))
print(answer_3 == 75)

answer_4 = int(input("How many letters does the word Dad have\n>"))
print(answer_4 == 3)

answer_5 = int(input("Give me a number greater than 42 but less than 45\n"))
print(answer_5 > 42 and answer_5 < 45)

print("Well done completing the quiz!!!")