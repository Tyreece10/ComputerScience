#
import random
nums = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

#Generate a list of five random integers from 0-99

print(nums)

#Define function
def bubble_sort(numbers):   #Take the list as a parameter
    #Create a vari for steps, star at 0
    steps = 0   

    #Check if the list is sort as many times as their are list items
    for i in range(0, len(numbers) - 1):
        #Iterate through every item in the list
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            steps += 1

    print(numbers)
    print("Completed in "+str(steps) + " steps")

    print(numbers)
            

bubble_sort(nums)