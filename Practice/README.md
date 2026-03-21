# Python Practice Questions And Answers

1. Write a program to print:

`Hello, Python`

```py
print("Hello, Python")
```

1. Write a program to take your name as input and print `Welcome, <name>`.

```py
name = input("Enter Your Name : ")

print(f"Welcome, {name}")
```

1. Write a program to input two numbers and print their sum, difference, product, quotient, and remainder.

```py
num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))

print(f"Sum : {num_1 + num_2}")
print(f"Difference : {num_1 - num_2}")
print(f"Product : {num_1 * num_2}")

if num_2 != 0:
    print(f"Quotient : {num_1 / num_2}")
    print(f"Remainder : {num_1 % num_2}")
else:
    print("Quotient : Not Possible")
    print("Remainder : Not Possible")
```

1. Write a program to swap two numbers using a third variable.

```py
num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

temp = num_1
num_1 = num_2
num_2 = temp

print(f"Number 1 : {num_1}")
print(f"Number 2 : {num_2}")
```

1. Write a program to swap two numbers without using a third variable.

```py
num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

num_1 = num_1 + num_2
num_2 = num_1 - num_2
num_1 = num_1 - num_2

print(f"Number 1 : {num_1}")
print(f"Number 2 : {num_2}")
```

1. Write a program to input the radius of a circle and print its area and circumference.

```py
pi = 3.14159
radius = float(input("Enter Radius : "))

area = pi * radius * radius
circumference = 2 * pi * radius

print(f"Area : {area}")
print(f"Circumference : {circumference}")
```

1. Write a program to input marks of 5 subjects and print total, average, and percentage.

```py
marks = []

for index in range(1, 6):
    marks.append(float(input(f"Enter Marks Of Subject {index} : ")))

total = sum(marks)
average = total / len(marks)
percentage = total / 5

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Percentage : {percentage}")
```

1. Write a program to convert temperature from Celsius to Fahrenheit.

```py
celsius = float(input("Enter Temperature In Celsius : "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature In Fahrenheit : {fahrenheit}")
```

1. Write a program to input a number and print whether it is positive, negative, or zero.

```py
num = float(input("Enter A Number : "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

1. Write a program to check whether a number is even or odd.

```py
num = int(input("Enter A Number : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

1. Write a program to check whether a person is eligible to vote.

```py
age = int(input("Enter Age : "))

if age >= 18:
    print("Eligible To Vote")
else:
    print("Not Eligible To Vote")
```

1. Write a program to find the greater of two numbers.

```py
num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))

if num_1 > num_2:
    print(f"Greater Number : {num_1}")
else:
    print(f"Greater Number : {num_2}")
```

1. Write a program to find the greatest among three numbers.

```py
num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))
num_3 = float(input("Enter Number 3 : "))

greatest = num_1

if num_2 > greatest:
    greatest = num_2

if num_3 > greatest:
    greatest = num_3

print(f"Greatest Number : {greatest}")
```

1. Write a program to check whether a year is a leap year.

```py
year = int(input("Enter A Year : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
```

1. Write a program to check whether a character is a vowel or consonant.

```py
char = input("Enter A Character : ")

if char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

1. Write a program to check whether a number is divisible by both 5 and 11.

```py
num = int(input("Enter A Number : "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible By Both 5 And 11")
else:
    print("Not Divisible By Both 5 And 11")
```

1. Write a program to input a number and print its absolute value without using any built-in function.

```py
num = int(input("Enter A Number : "))

if num < 0:
    absolute_value = -num
else:
    absolute_value = num

print(f"Absolute Value : {absolute_value}")
```

1. Write a program to find whether a given number lies between 1 and 100.

```py
num = int(input("Enter A Number : "))

if 1 <= num <= 100:
    print("The Number Lies Between 1 And 100")
else:
    print("The Number Does Not Lie Between 1 And 100")
```

1. Write a program to print numbers from 1 to 10 using a loop.

```py
for number in range(1, 11):
    print(number)
```

1. Write a program to print numbers from 10 to 1 in reverse order.

```py
for number in range(10, 0, -1):
    print(number)
```

1. Write a program to print all even numbers from 1 to n.

```py
limit = int(input("Enter A Number : "))

for number in range(2, limit + 1, 2):
    print(number)
```

1. Write a program to print all odd numbers from 1 to n.

```py
limit = int(input("Enter A Number : "))

for number in range(1, limit + 1, 2):
    print(number)
```

1. Write a program to find the sum of first n natural numbers.

```py
limit = int(input("Enter A Number : "))
total = 0

for number in range(1, limit + 1):
    total += number

print(f"Sum : {total}")
```

1. Write a program to find the factorial of a number.

```py
num = int(input("Enter A Number : "))
factorial = 1

for number in range(1, num + 1):
    factorial *= number

print(f"Factorial : {factorial}")
```

1. Write a program to print the multiplication table of a given number.

```py
num = int(input("Enter A Number : "))

for number in range(1, 11):
    print(f"{num} X {number} = {num * number}")
```

1. Write a program to count how many digits are present in a number.

```py
num = int(input("Enter A Number : "))
count = 0

if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        count += 1
        num //= 10

print(f"Digit Count : {count}")
```

1. Write a program to find the sum of digits of a number.

```py
num = int(input("Enter A Number : "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

print(f"Sum Of Digits : {total}")
```

1. Write a program to reverse a number.

```py
num = int(input("Enter A Number : "))
sign = -1 if num < 0 else 1
num = abs(num)
reversed_num = 0

while num > 0:
    reversed_num = (reversed_num * 10) + (num % 10)
    num //= 10

print(f"Reversed Number : {reversed_num * sign}")
```

1. Write a program to check whether a number is a palindrome.

```py
num = int(input("Enter A Number : "))
original_num = abs(num)
temp = original_num
reversed_num = 0

while temp > 0:
    reversed_num = (reversed_num * 10) + (temp % 10)
    temp //= 10

if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")
```

1. Write a program to check whether a number is an Armstrong number.

```py
num = int(input("Enter A Number : "))
digits = str(abs(num))
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if total == abs(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

1. Write a program to print all Armstrong numbers between 1 and 1000.

```py
for number in range(1, 1001):
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == number:
        print(number)
```

1. Write a program to check whether a number is prime.

```py
num = int(input("Enter A Number : "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True

    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
```

1. Write a program to print all prime numbers in a given range.

```py
start = int(input("Enter Start Number : "))
end = int(input("Enter End Number : "))

for number in range(start, end + 1):
    if number < 2:
        continue

    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
```

1. Write a program to find the HCF of two numbers.

```py
num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

a = abs(num_1)
b = abs(num_2)

while b != 0:
    a, b = b, a % b

print(f"HCF : {a}")
```

1. Write a program to find the LCM of two numbers.

```py
num_1 = int(input("Enter Number 1 : "))
num_2 = int(input("Enter Number 2 : "))

greater = max(abs(num_1), abs(num_2))
lcm = greater

while True:
    if lcm % num_1 == 0 and lcm % num_2 == 0:
        print(f"LCM : {lcm}")
        break
    lcm += greater
```

1. Write a program to print the Fibonacci series up to n terms.

```py
terms = int(input("Enter Number Of Terms : "))
first = 0
second = 1

for _ in range(terms):
    print(first)
    first, second = second, first + second
```

1. Write a program to keep taking numbers as input until the user enters 0, then print their sum.

```py
total = 0

while True:
    num = float(input("Enter A Number : "))
    if num == 0:
        break
    total += num

print(f"Sum : {total}")
```

1. Write a program to repeatedly ask for a password until the correct password is entered.

```py
correct_password = "python123"

while True:
    password = input("Enter Password : ")
    if password == correct_password:
        print("Correct Password")
        break
    print("Wrong Password")
```

1. Write a program to print a right-aligned triangle of stars.

```py
rows = int(input("Enter Number Of Rows : "))

for row in range(1, rows + 1):
    print(" " * (rows - row) + "*" * row)
```

1. Write a program to count how many numbers between 1 and n are divisible by 3 but not by 5.

```py
limit = int(input("Enter A Number : "))
count = 0

for number in range(1, limit + 1):
    if number % 3 == 0 and number % 5 != 0:
        count += 1

print(f"Count : {count}")
```

1. Write a program to print the first n numbers that are divisible by 7.

```py
count = int(input("Enter A Number : "))
number = 7
printed = 0

while printed < count:
    print(number)
    number += 7
    printed += 1
```

1. Write a program to input a string and print it character by character.

```py
text = input("Enter A String : ")

for char in text:
    print(char)
```

1. Write a program to count the number of vowels, consonants, digits, and spaces in a string.

```py
text = input("Enter A String : ")
vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1

print(f"Vowels : {vowels}")
print(f"Consonants : {consonants}")
print(f"Digits : {digits}")
print(f"Spaces : {spaces}")
```

1. Write a program to reverse a string without using slicing.

```py
text = input("Enter A String : ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)
```

1. Write a program to check whether a string is a palindrome.

```py
text = input("Enter A String : ")
clean_text = text.lower()
reversed_text = ""

for char in clean_text:
    reversed_text = char + reversed_text

if clean_text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")
```

1. Write a program to count the occurrence of a given character in a string.

```py
text = input("Enter A String : ")
target = input("Enter A Character : ")
count = 0

for char in text:
    if char == target:
        count += 1

print(f"Occurrence : {count}")
```

1. Write a program to count the number of words in a sentence.

```py
sentence = input("Enter A Sentence : ")
words = sentence.split()

print(f"Word Count : {len(words)}")
```

1. Write a program to convert a string to uppercase without using upper().

```py
text = input("Enter A String : ")
result = ""

for char in text:
    code = ord(char)
    if 97 <= code <= 122:
        result += chr(code - 32)
    else:
        result += char

print(result)
```

1. Write a program to convert a string to lowercase without using lower().

```py
text = input("Enter A String : ")
result = ""

for char in text:
    code = ord(char)
    if 65 <= code <= 90:
        result += chr(code + 32)
    else:
        result += char

print(result)
```

1. Write a program to remove all spaces from a string.

```py
text = input("Enter A String : ")
result = ""

for char in text:
    if char != " ":
        result += char

print(result)
```

1. Write a program to find the longest word in a sentence.

```py
sentence = input("Enter A Sentence : ")
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest Word : {longest_word}")
```

1. Write a program to replace every occurrence of one word in a sentence with another word.

```py
sentence = input("Enter A Sentence : ")
old_word = input("Enter Word To Replace : ")
new_word = input("Enter New Word : ")

print(sentence.replace(old_word, new_word))
```

1. Write a program to check whether two strings are anagrams.

```py
text_1 = input("Enter String 1 : ").replace(" ", "").lower()
text_2 = input("Enter String 2 : ").replace(" ", "").lower()

if sorted(text_1) == sorted(text_2):
    print("Anagrams")
else:
    print("Not Anagrams")
```

1. Write a program to print only the characters at even positions in a string.

```py
text = input("Enter A String : ")

for index in range(1, len(text), 2):
    print(text[index])
```

1. Write a program to create a list of 10 integers from user input and print the largest and smallest values.

```py
numbers = []

for index in range(1, 11):
    numbers.append(int(input(f"Enter Number {index} : ")))

print(f"Largest : {max(numbers)}")
print(f"Smallest : {min(numbers)}")
```

1. Write a program to find the sum of all elements in a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]

print(f"Sum : {sum(numbers)}")
```

1. Write a program to count how many even and odd numbers are present in a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even Count : {even_count}")
print(f"Odd Count : {odd_count}")
```

1. Write a program to remove all duplicate elements from a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
```

1. Write a program to sort a list in ascending order without using sort().

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]

for index in range(len(numbers)):
    for inner_index in range(index + 1, len(numbers)):
        if numbers[index] > numbers[inner_index]:
            numbers[index], numbers[inner_index] = numbers[inner_index], numbers[index]

print(numbers)
```

1. Write a program to merge two lists into one.

```py
list_1 = [int(value) for value in input("Enter First List : ").split()]
list_2 = [int(value) for value in input("Enter Second List : ").split()]

print(list_1 + list_2)
```

1. Write a program to find the second largest element in a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("Second Largest Element Does Not Exist")
else:
    unique_numbers.sort()
    print(f"Second Largest : {unique_numbers[-2]}")
```

1. Write a program to rotate a list to the right by one position.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]

if numbers:
    numbers = [numbers[-1]] + numbers[:-1]

print(numbers)
```

1. Write a program to separate positive and negative numbers from a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
positive_numbers = []
negative_numbers = []

for number in numbers:
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(f"Positive Numbers : {positive_numbers}")
print(f"Negative Numbers : {negative_numbers}")
```

1. Write a program to count the frequency of each element in a list.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
```

1. Write a program to find the common elements in two lists.

```py
list_1 = [int(value) for value in input("Enter First List : ").split()]
list_2 = [int(value) for value in input("Enter Second List : ").split()]
common_elements = []

for number in list_1:
    if number in list_2 and number not in common_elements:
        common_elements.append(number)

print(common_elements)
```

1. Write a program to read n numbers into a list and print only those numbers that are prime.

```py
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


count = int(input("Enter How Many Numbers : "))
numbers = []

for index in range(1, count + 1):
    numbers.append(int(input(f"Enter Number {index} : ")))

for number in numbers:
    if is_prime(number):
        print(number)
```

1. Write a program to create a tuple with five elements and print each element separately.

```py
items = tuple(input("Enter Five Elements : ").split())

for item in items[:5]:
    print(item)
```

1. Write a program to find the maximum and minimum element in a tuple.

```py
items = tuple(int(value) for value in input("Enter Tuple Values : ").split())

print(f"Maximum : {max(items)}")
print(f"Minimum : {min(items)}")
```

1. Write a program to count how many times a given item appears in a tuple.

```py
items = tuple(input("Enter Tuple Values : ").split())
target = input("Enter Item To Count : ")

print(f"Count : {items.count(target)}")
```

1. Write a program to convert a list into a tuple and a tuple into a list.

```py
list_values = input("Enter List Values : ").split()
tuple_values = tuple(list_values)
tuple_input = tuple(input("Enter Tuple Values : ").split())
list_from_tuple = list(tuple_input)

print(f"Tuple : {tuple_values}")
print(f"List : {list_from_tuple}")
```

1. Write a program to take student names as keys and marks as values, then print the dictionary.

```py
count = int(input("Enter Number Of Students : "))
students = {}

for index in range(1, count + 1):
    name = input(f"Enter Student {index} Name : ")
    marks = float(input(f"Enter {name} Marks : "))
    students[name] = marks

print(students)
```

1. Write a program to input a dictionary and print all keys, all values, and all key-value pairs separately.

```py
count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

print("Keys")
for key in data.keys():
    print(key)

print("Values")
for value in data.values():
    print(value)

print("Key Value Pairs")
for key, value in data.items():
    print(key, value)
```

1. Write a program to find the student with the highest marks from a dictionary.

```py
count = int(input("Enter Number Of Students : "))
students = {}

for index in range(1, count + 1):
    name = input(f"Enter Student {index} Name : ")
    marks = float(input(f"Enter {name} Marks : "))
    students[name] = marks

top_student = max(students, key=students.get)

print(f"Highest Marks Student : {top_student}")
print(f"Marks : {students[top_student]}")
```

1. Write a program to count the frequency of each character in a string using a dictionary.

```py
text = input("Enter A String : ")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```

1. Write a program to merge two dictionaries.

```py
count_1 = int(input("Enter Number Of Items In First Dictionary : "))
dict_1 = {}

for index in range(1, count_1 + 1):
    key = input(f"Enter First Dictionary Key {index} : ")
    value = input(f"Enter First Dictionary Value {index} : ")
    dict_1[key] = value

count_2 = int(input("Enter Number Of Items In Second Dictionary : "))
dict_2 = {}

for index in range(1, count_2 + 1):
    key = input(f"Enter Second Dictionary Key {index} : ")
    value = input(f"Enter Second Dictionary Value {index} : ")
    dict_2[key] = value

merged = dict_1.copy()
merged.update(dict_2)

print(merged)
```

1. Write a program to check whether a given key exists in a dictionary.

```py
count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

target_key = input("Enter Key To Search : ")

if target_key in data:
    print("Key Exists")
else:
    print("Key Does Not Exist")
```

1. Write a program to invert a dictionary so that values become keys.

```py
count = int(input("Enter Number Of Items : "))
data = {}

for index in range(1, count + 1):
    key = input(f"Enter Key {index} : ")
    value = input(f"Enter Value {index} : ")
    data[key] = value

inverted = {}

for key, value in data.items():
    inverted[value] = key

print(inverted)
```

1. Write a function to check whether a number is prime.

```py
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


num = int(input("Enter A Number : "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
```

1. Write a function to return the factorial of a number.

```py
def factorial(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


num = int(input("Enter A Number : "))
print(f"Factorial : {factorial(num)}")
```

1. Write a function to return the sum of digits of a number.

```py
def sum_of_digits(number):
    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


num = int(input("Enter A Number : "))
print(f"Sum Of Digits : {sum_of_digits(num)}")
```

1. Write a function that accepts a list and returns the largest element.

```py
def largest_element(items):
    largest = items[0]

    for item in items:
        if item > largest:
            largest = item

    return largest


numbers = [int(value) for value in input("Enter Numbers : ").split()]
print(f"Largest Element : {largest_element(numbers)}")
```

1. Write a function that accepts a string and returns the number of vowels in it.

```py
def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count


text = input("Enter A String : ")
print(f"Vowel Count : {count_vowels(text)}")
```

1. Write a function with default arguments to calculate simple interest.

```py
def simple_interest(principal, rate=5, time=1):
    return (principal * rate * time) / 100


principal = float(input("Enter Principal : "))
rate_text = input("Enter Rate Or Press Enter : ")
time_text = input("Enter Time Or Press Enter : ")

rate = float(rate_text) if rate_text else 5
time = float(time_text) if time_text else 1

print(f"Simple Interest : {simple_interest(principal, rate, time)}")
```

1. Write a function that accepts any number of arguments and returns their sum.

```py
def total_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


values = [int(value) for value in input("Enter Numbers : ").split()]
print(f"Sum : {total_sum(*values)}")
```

1. Write a recursive function to find the factorial of a number.

```py
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


num = int(input("Enter A Number : "))
print(f"Factorial : {factorial(num)}")
```

1. Write a recursive function to print Fibonacci terms up to n.

```py
def fibonacci(terms, first=0, second=1):
    if terms <= 0:
        return

    print(first)
    fibonacci(terms - 1, second, first + second)


terms = int(input("Enter Number Of Terms : "))
fibonacci(terms)
```

1. Write a lambda expression to square a number.

```py
square = lambda number: number * number

num = float(input("Enter A Number : "))
print(f"Square : {square(num)}")
```

1. Write a lambda expression to find the larger of two numbers.

```py
larger = lambda first, second: first if first > second else second

num_1 = float(input("Enter Number 1 : "))
num_2 = float(input("Enter Number 2 : "))

print(f"Larger Number : {larger(num_1, num_2)}")
```

1. Write a program to generate 10 random numbers between 1 and 100.

```py
import random


for _ in range(10):
    print(random.randint(1, 100))
```

1. Write a program to simulate rolling a die 20 times.

```py
import random


for _ in range(20):
    print(random.randint(1, 6))
```

1. Write a program to choose a random item from a list.

```py
import random


items = input("Enter List Items : ").split()

if items:
    print(random.choice(items))
else:
    print("List Is Empty")
```

1. Write a program that uses the math library to compute square root, power, floor, and ceil of a number.

```py
import math


num = float(input("Enter A Number : "))
power = float(input("Enter Power : "))

print(f"Square Root : {math.sqrt(num)}")
print(f"Power : {math.pow(num, power)}")
print(f"Floor : {math.floor(num)}")
print(f"Ceil : {math.ceil(num)}")
```

1. Write a program that creates a file and writes 5 lines of text into it.

```py
file_name = "file_93.txt"

with open(file_name, "w") as file:
    for index in range(1, 6):
        file.write(f"Line {index}\n")

print(f"Data Written To {file_name}")
```

1. Write a program to read a file and print its contents line by line.

```py
file_name = input("Enter File Name : ")

with open(file_name, "r") as file:
    for line in file:
        print(line.rstrip())
```

1. Write a program to count the number of lines, words, and characters in a file.

```py
file_name = input("Enter File Name : ")

with open(file_name, "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print(f"Lines : {len(lines)}")
print(f"Words : {len(words)}")
print(f"Characters : {characters}")
```

1. Write a program to copy the contents of one file into another.

```py
source_file = input("Enter Source File Name : ")
target_file = input("Enter Target File Name : ")

with open(source_file, "r") as source:
    content = source.read()

with open(target_file, "w") as target:
    target.write(content)

print("File Copied")
```

1. Write a program to read a file and print only those lines that contain a given word.

```py
file_name = input("Enter File Name : ")
target_word = input("Enter Word To Search : ")

with open(file_name, "r") as file:
    for line in file:
        if target_word in line:
            print(line.rstrip())
```

1. Write a program to append new data to an existing file.

```py
file_name = input("Enter File Name : ")
data = input("Enter Data To Append : ")

with open(file_name, "a") as file:
    file.write(data + "\n")

print("Data Appended")
```

1. Write a program to store a list of numbers in a file, then read them back and print their sum.

```py
file_name = "numbers_99.txt"
numbers = [int(value) for value in input("Enter Numbers : ").split()]

with open(file_name, "w") as file:
    for number in numbers:
        file.write(f"{number}\n")

total = 0

with open(file_name, "r") as file:
    for line in file:
        total += int(line.strip())

print(f"Sum : {total}")
```

1. Write a program that asks the user for a filename and handles the case where the file does not exist.

```py
file_name = input("Enter File Name : ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Does Not Exist")
```

1. Write a program that takes two numbers and handles division by zero properly.

```py
try:
    num_1 = float(input("Enter Number 1 : "))
    num_2 = float(input("Enter Number 2 : "))
    print(f"Result : {num_1 / num_2}")
except ZeroDivisionError:
    print("Division By Zero Is Not Allowed")
```

1. Write a program that takes an integer input and handles invalid input using exception handling.

```py
try:
    num = int(input("Enter An Integer : "))
    print(f"You Entered : {num}")
except ValueError:
    print("Invalid Integer Input")
```

1. Create your own exception for checking whether a number is negative where only positive numbers are allowed.

```py
class NegativeNumberError(Exception):
    pass


num = int(input("Enter A Positive Number : "))

if num < 0:
    raise NegativeNumberError("Negative Numbers Are Not Allowed")

print("Valid Number")
```

1. Write a menu-driven calculator using functions for add, subtract, multiply, and divide.

```py
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return "Division By Zero Is Not Allowed"
    return first / second


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "5":
        break

    num_1 = float(input("Enter Number 1 : "))
    num_2 = float(input("Enter Number 2 : "))

    if choice == "1":
        print(add(num_1, num_2))
    elif choice == "2":
        print(subtract(num_1, num_2))
    elif choice == "3":
        print(multiply(num_1, num_2))
    elif choice == "4":
        print(divide(num_1, num_2))
    else:
        print("Invalid Choice")
```

1. Write a menu-driven program for these operations on a list: insert, delete, search, display.

```py
items = []

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        value = input("Enter Value : ")
        items.append(value)
    elif choice == "2":
        value = input("Enter Value To Delete : ")
        if value in items:
            items.remove(value)
        else:
            print("Value Not Found")
    elif choice == "3":
        value = input("Enter Value To Search : ")
        if value in items:
            print(f"Found At Position : {items.index(value)}")
        else:
            print("Value Not Found")
    elif choice == "4":
        print(items)
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
```

1. Write a program to maintain a student record using a dictionary with options to add, update, delete, and display.

```py
students = {}

while True:
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        name = input("Enter Student Name : ")
        marks = float(input("Enter Marks : "))
        students[name] = marks
    elif choice == "2":
        name = input("Enter Student Name : ")
        if name in students:
            students[name] = float(input("Enter New Marks : "))
        else:
            print("Student Not Found")
    elif choice == "3":
        name = input("Enter Student Name : ")
        if name in students:
            del students[name]
        else:
            print("Student Not Found")
    elif choice == "4":
        print(students)
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
```

1. Write a program to count uppercase letters, lowercase letters, digits, and special characters in a string.

```py
text = input("Enter A String : ")
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"Uppercase : {upper_count}")
print(f"Lowercase : {lower_count}")
print(f"Digits : {digit_count}")
print(f"Special Characters : {special_count}")
```

1. Write a program to print the following series up to n terms:

`1, 8, 27, 64, 125, ...`

```py
terms = int(input("Enter Number Of Terms : "))

for number in range(1, terms + 1):
    print(number ** 3)
```

1. Write a program to check whether a given number is a strong number.

```py
def factorial(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


num = int(input("Enter A Number : "))
original_num = num
total = 0

while num > 0:
    digit = num % 10
    total += factorial(digit)
    num //= 10

if total == original_num:
    print("Strong Number")
else:
    print("Not Strong Number")
```

1. Write a program to check whether a string contains only digits.

```py
text = input("Enter A String : ")

if text.isdigit():
    print("Contains Only Digits")
else:
    print("Does Not Contain Only Digits")
```

1. Write a program to remove all punctuation marks from a string.

```py
import string


text = input("Enter A String : ")
result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print(result)
```

1. Write a program to print the transpose of a 2D list representing a matrix.

```py
rows = int(input("Enter Number Of Rows : "))
columns = int(input("Enter Number Of Columns : "))
matrix = []

for row in range(rows):
    current_row = [int(value) for value in input(f"Enter Row {row + 1} : ").split()]
    matrix.append(current_row)

transpose = []

for column in range(columns):
    current_row = []
    for row in range(rows):
        current_row.append(matrix[row][column])
    transpose.append(current_row)

for row in transpose:
    print(row)
```

1. Write a program to add two matrices.

```py
rows = int(input("Enter Number Of Rows : "))
columns = int(input("Enter Number Of Columns : "))
matrix_1 = []
matrix_2 = []

for row in range(rows):
    matrix_1.append([int(value) for value in input(f"Enter First Matrix Row {row + 1} : ").split()])

for row in range(rows):
    matrix_2.append([int(value) for value in input(f"Enter Second Matrix Row {row + 1} : ").split()])

result = []

for row in range(rows):
    current_row = []
    for column in range(columns):
        current_row.append(matrix_1[row][column] + matrix_2[row][column])
    result.append(current_row)

for row in result:
    print(row)
```

1. Write a program to multiply two matrices.

```py
rows_1 = int(input("Enter First Matrix Rows : "))
columns_1 = int(input("Enter First Matrix Columns : "))
matrix_1 = []

for row in range(rows_1):
    matrix_1.append([int(value) for value in input(f"Enter First Matrix Row {row + 1} : ").split()])

rows_2 = int(input("Enter Second Matrix Rows : "))
columns_2 = int(input("Enter Second Matrix Columns : "))
matrix_2 = []

for row in range(rows_2):
    matrix_2.append([int(value) for value in input(f"Enter Second Matrix Row {row + 1} : ").split()])

if columns_1 != rows_2:
    print("Matrix Multiplication Is Not Possible")
else:
    result = []

    for row in range(rows_1):
        current_row = []
        for column in range(columns_2):
            total = 0
            for index in range(columns_1):
                total += matrix_1[row][index] * matrix_2[index][column]
            current_row.append(total)
        result.append(current_row)

    for row in result:
        print(row)
```

1. Write a program to search for an element in a list and print its position. If not found, print an appropriate message.

```py
numbers = [int(value) for value in input("Enter Numbers : ").split()]
target = int(input("Enter Number To Search : "))

if target in numbers:
    print(f"Position : {numbers.index(target) + 1}")
else:
    print("Element Not Found")
```

1. Write a function to return the count of uppercase and lowercase letters in a string.

```py
def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


text = input("Enter A String : ")
uppercase_count, lowercase_count = count_letters(text)

print(f"Uppercase : {uppercase_count}")
print(f"Lowercase : {lowercase_count}")
```

1. Write a function that takes a list and returns a new list containing only unique elements in the same order.

```py
def unique_elements(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


items = input("Enter Items : ").split()
print(unique_elements(items))
```

1. Write a function that accepts a sentence and returns a dictionary containing each word and its frequency.

```py
def word_frequency(sentence):
    frequency = {}

    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


sentence = input("Enter A Sentence : ")
print(word_frequency(sentence))
```

1. Write a program that stores attendance of students as `Present` or `Absent` and counts how many are present.

```py
count = int(input("Enter Number Of Students : "))
attendance = {}

for index in range(1, count + 1):
    name = input(f"Enter Student {index} Name : ")
    status = input(f"Enter Attendance For {name} : ")
    attendance[name] = status

present_count = 0

for status in attendance.values():
    if status.lower() == "present":
        present_count += 1

print(attendance)
print(f"Present Count : {present_count}")
```

1. Write a program to create a billing system for n items where input is item name, quantity, and price, then print total bill.

```py
count = int(input("Enter Number Of Items : "))
total_bill = 0

for index in range(1, count + 1):
    item_name = input(f"Enter Item {index} Name : ")
    quantity = int(input(f"Enter Quantity Of {item_name} : "))
    price = float(input(f"Enter Price Of {item_name} : "))
    amount = quantity * price
    total_bill += amount
    print(f"{item_name} : {amount}")

print(f"Total Bill : {total_bill}")
```

1. Write a program to generate a random password of given length using letters and digits.

```py
import random
import string


length = int(input("Enter Password Length : "))
characters = string.ascii_letters + string.digits
password = ""

for _ in range(length):
    password += random.choice(characters)

print(password)
```

1. Write a program to validate a password using rules such as minimum length, at least one uppercase letter, one lowercase letter, one digit, and one special character.

```py
password = input("Enter Password : ")
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")
```
