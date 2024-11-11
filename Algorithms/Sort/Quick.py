def quicksort(lst):
    if len(lst) <= 1:  # Base case
        return lst

    pivot = lst[-1]  # Choose the last element as pivot
    left = [x for x in lst[:-1] if x < pivot]      # Elements less than pivot
    right = [x for x in lst[:-1] if x >= pivot]    # Elements greater than or equal to pivot

    # Recursively apply quicksort to the left and right parts
    return quicksort(left) + [pivot] + quicksort(right)




print(quicksort([8,2,4,7,1,3,9,6,5]))