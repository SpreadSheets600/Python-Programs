# Program 6 : Tuples are immutable. Replace an element by converting the tuple to a list and back.

tup = (1, 2, 3, 4, 5)
lst = list(tup)

lst[2] = 99
tup = tuple(lst)

print("Modified Tuple : ", tup)
