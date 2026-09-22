# Write a program to merge two dictionaries into one. If a key is present in both, sum their values.

d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}

merged = d1.copy()

for key, value in d2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("Merged Dictionary :", merged)
