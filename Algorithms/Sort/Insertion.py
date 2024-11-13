def insertion(lst):
    for j in range(1, len(lst)):
        temp = lst[j]
        i = j
        # Move elements of lst[0..i-1], that are greater than temp, one position ahead
        while i > 0 and lst[i-1] > temp:
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = temp  # Insert the element at its correct position
    return lst

print(insertion([6, 1, 7, 4, 2, 9, 8, 5, 3]))
