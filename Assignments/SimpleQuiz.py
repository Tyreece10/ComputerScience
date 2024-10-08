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

def tally_score():
    score = 0
    if answer > 499:
        score = score + 1
    if answer_two < 11 and answer_two > 5:
        score = score + 1
    if answer_three == 75:
        score = score + 1
    if answer_four == 3:
        score = score + 1
    if answer_five > 42 and answer_five < 45:
        score = score + 1
    print("Your score is")
    print(score)

tally_score()
