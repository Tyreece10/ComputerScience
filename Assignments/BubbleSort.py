
def bubble_sort(a, b, c, d, e, f):
    list = [a, b, c, d, e, f]
    steps = 0  # To count the number of steps
    n = len(list)
    
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1  # steps count
            if list[j] > list[j+1]:
                # Swap
                list[j], list[j+1] = list[j+1], list[j]
    
    print(f"Number of steps: {steps}")
    return list

# Example usage
sorted_list = bubble_sort(12, 25, 8, 24, 32, 64)
print("Sorted List:", sorted_list)
