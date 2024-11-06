def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    # Sort left and right parts using quick_sort itself
    return quick_sort(left) + middle + quick_sort(right)

# Function to sort the elements passed as individual arguments
def sort_elements(a, b, c, d, e, f):
    lst = [a, b, c, d, e, f]
    sorted_lst = quick_sort(lst)
    return sorted_lst

# Example usage
sorted_list = sort_elements(3, 12, 60, 20, 43, 34)
print("Sorted List:", sorted_list)




def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)