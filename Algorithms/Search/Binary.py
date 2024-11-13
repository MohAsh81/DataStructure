def binarysearch(lst, elm):
    lst = sorted(lst)
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == elm:
            return mid
        elif lst[mid] < elm:
            left = mid + 1
        else:
            right = mid - 1

    return None  # Element not found
