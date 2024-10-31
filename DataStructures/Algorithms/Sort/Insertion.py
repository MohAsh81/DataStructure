def insertion(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i
        # Move elements of lst[0..i-1], that are greater than temp, one position ahead
        while j > 0 and lst[j-1] > temp:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = temp  # Insert the element at its correct position
    return lst

print(insertion([6, 1, 7, 4, 2, 9, 8, 5, 3]))
