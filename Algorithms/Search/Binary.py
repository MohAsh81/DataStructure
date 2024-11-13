def binarysearch(lst, elm):
    def search_helper(lst, elm, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2

        if lst[mid] == elm:
            return mid
        elif lst[mid] < elm:
            return search_helper(lst, elm, mid + 1, right)
        else:
            return search_helper(lst, elm, left, mid - 1)

    # Assuming list is sorted, or sort it once outside.
    lst = sorted(lst)
    return search_helper(lst, elm, 0, len(lst) - 1)


print(binarysearch([1, 5, 7, 2, 4, 9, 0, 6, 10, 3, 8], 3))
