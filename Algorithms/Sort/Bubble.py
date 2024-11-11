def bubblesort(lst):
    temp = 0
    mx = len(lst)
    for j in range(mx):
        for i in range(mx):
            if i+1 < mx:
                if lst[i] > lst[i+1]:
                    temp = lst[i+1]
                    lst[i+1] = lst[i]
                    lst[i] = temp
                else:
                    pass
            else:
                pass
    return lst


print(bubblesort([9, 1, 8, 2,7,3,6,4,5]))
