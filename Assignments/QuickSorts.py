#
import random
numbers = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

#Generate a list of five random integers from 0-99

print(numbers)

# [9, 3, 5, 2, 6, 7, 3]

def quick_sort(n):
    #Set pivot as the last number
    lPos = 0
    rPos = len(n)-1

    pivot = n[-1]
 #first number from the left that is LARGER     l
 #First number from the right that is SMALLER       r

    for j in range(0, len(n)):
        #Find L
        for i in range(0, len(n)):
            if n[1]  > pivot:
                l = n[i]
                lPos = i
                break                   #


    #Find r
        for i in range(len(n)-1, -1, -1):
            if n[i] < pivot:
                rPos = i
                break
        #Check if l index is greater than r index
        if lPos > rPos:
            #Switch pivot with item from left
            n[lPos], n[-1] = n[-1], n[lPos]
            break
        else:    

            #Swap l and r values
            n[lPos], n[rPos] = n[rPos], n[lPos]

    print(n)


quick_sort(numbers)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)