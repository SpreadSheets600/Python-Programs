items = {"pen": 10, "notebook": 50, "eraser": 5, "pencil": 7, "bag": 300}

print("Original Dictionary :", items)

sorted_by_keys = dict(sorted(items.items()))
print("\nSorted By Keys :", sorted_by_keys)

sorted_by_values = dict(sorted(items.items(), key=lambda x: x[1]))
print("\nSorted By Values:", sorted_by_values)
