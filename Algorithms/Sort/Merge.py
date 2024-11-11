def merge_sort(lst):
    if len(lst) <= 1:  # Base case for recursion
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])  # Recursively sort the left half
    right_half = merge_sort(lst[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements, if any
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


print(merge_sort([3, 7, 8, 5, 4, 2, 6, 1]))
