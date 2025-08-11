# WAP To Count How Many Times An Element Occurs In A List

lst = [1, 2, 3, 4, 5, 3, 2, 1]

element_to_count = 3
count_of_element = lst.count(element_to_count)

print(f"The Element {element_to_count} Occurs : ", count_of_element)

# Taking User Input (Eval)

lst = eval(input("Enter A List Of Numbers : "))
element_to_count = int(input("Enter The Element To Count : "))

count_of_element = lst.count(element_to_count)

print(f"The Element {element_to_count} Occurs : ", count_of_element)
