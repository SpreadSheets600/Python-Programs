def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

lst = [5, 2, 9, 1, 5, 6]
sorted_lst = bubbleSort(lst)
print("Sorted List :", sorted_lst)

