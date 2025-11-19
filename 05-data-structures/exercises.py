"""
EXERCISES - DATA STRUCTURES
============================
Follow the instructions below. Comment out exercises you're not working on.
Run the program after each exercise to test your solution.
"""

# ============================================================================
# EXERCISE 1: Lists - Add and Remove
print("\n" + "=" * 60)
print("EXERCISE 1: Lists - Add and Remove")
print("=" * 60)
# ============================================================================
# Create an empty list called fruits
# Add "apple", "banana", and "cherry" to the list
# Remove "banana"
# Print the list
# Expected output: ['apple', 'cherry']


# YOUR CODE HERE:
fruits = []

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.remove("banana")

print(fruits)


# ============================================================================
# EXERCISE 2: Finding Items in Lists
print("\n" + "=" * 60)
print("EXERCISE 2: Finding Items in Lists")
print("=" * 60)
# ============================================================================
# Create a list: numbers = [10, 20, 30, 40, 50]
# Find and print the index of the number 30
# Check if 60 is in the list (print True or False)
# Expected output:
# 2
# False


# YOUR CODE HERE:
numbers = [10, 20, 30, 40, 50]

print(numbers.index(30) if 30 in numbers else "30 is not in the list")
print(60 in numbers)

# ============================================================================
# EXERCISE 3: Sorting Lists
print("\n" + "=" * 60)
print("EXERCISE 3: Sorting Lists")
print("=" * 60)
# ============================================================================
# Create a list: prices = [50, 20, 80, 15, 40]
# Sort the list in ascending order (modify the original list)
# Print the sorted list
# Sort in descending order and print again
# Expected output:
# [15, 20, 40, 50, 80]
# [80, 50, 40, 20, 15]


# YOUR CODE HERE:
prices = [50, 20, 80, 15, 40]

# ascending
prices.sort()
print(prices)

# descending
prices.sort(reverse=True)
print(prices)


# ============================================================================
# EXERCISE 4: Stack (LIFO)
print("\n" + "=" * 60)
print("EXERCISE 4: Stack (LIFO)")
print("=" * 60)
# ============================================================================
# Create an empty stack (list)
# Push "action1", "action2", "action3" onto the stack
# Pop the last action and print it
# Print the remaining stack
# Expected output:
# action3
# ['action1', 'action2']


# YOUR CODE HERE:
stack = []

stack.append("action1")
stack.append("action2")
stack.append("action3")

last = stack.pop()

print(last)
print(stack)

# ============================================================================
# EXERCISE 5: Queue (FIFO)
print("\n" + "=" * 60)
print("EXERCISE 5: Queue (FIFO)")
print("=" * 60)
# ============================================================================
# Import deque from collections
# Create a queue with ["customer1", "customer2", "customer3"]
# Remove the first customer (dequeue)
# Add "customer4" to the queue
# Print the queue
# Expected output: deque(['customer2', 'customer3', 'customer4'])


# YOUR CODE HERE:
from collections import deque

queue = deque(["customer1", "customer2", "customer3"])

queue.popleft()
queue.append("customer4")

print(queue)

# ============================================================================
# EXERCISE 6: Tuple Unpacking
print("\n" + "=" * 60)
print("EXERCISE 6: Tuple Unpacking")
print("=" * 60)
# ============================================================================
# Create a tuple: coordinates = (10, 20, 30)
# Unpack it into variables x, y, z
# Print each variable
# Expected output:
# 10
# 20
# 30


# YOUR CODE HERE:
cordinates = (10, 20, 30)
x, y, z = cordinates

print(x)
print(y)
print(z)


# ============================================================================
# EXERCISE 7: Swapping Variables
print("\n" + "=" * 60)
print("EXERCISE 7: Swapping Variables")
print("=" * 60)
# ============================================================================
# Create two variables: a = 5, b = 10
# Swap their values using tuple unpacking
# Print both variables
# Expected output:
# a = 10
# b = 5


# YOUR CODE HERE:
a = 5
b = 10

a, b = b, a

print("a:", a)
print("b:", b)


# ============================================================================
# EXERCISE 8: Arrays
print("\n" + "=" * 60)
print("EXERCISE 8: Arrays")
print("=" * 60)
# ============================================================================
# Import array from array module
# Create an integer array with values [1, 2, 3, 4, 5]
# Append 6 to the array
# Print the array
# Expected output: array('i', [1, 2, 3, 4, 5, 6])


# YOUR CODE HERE:
from array import array

values = array("i", [1, 2, 3, 4, 5])

values.append(6)

print("values:", values)

# ============================================================================
# EXERCISE 9: Sets - Remove Duplicates
print("\n" + "=" * 60)
print("EXERCISE 9: Sets - Remove Duplicates")
print("=" * 60)
# ============================================================================
# Create a list: numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Convert it to a set to remove duplicates
# Convert back to a sorted list
# Print the result
# Expected output: [1, 2, 3, 4, 5]


# YOUR CODE HERE:
numbers = [1, 3, 3, 2, 2, 3, 4, 5, 5]
print(sorted(list(set(numbers))))

# ============================================================================
# EXERCISE 10: Set Operations
print("\n" + "=" * 60)
print("EXERCISE 10: Set Operations")
print("=" * 60)
# ============================================================================
# Create two sets:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# Find and print:
# a) Union (all unique items)
# b) Intersection (common items)
# c) Difference (items in set1 but not in set2)
# Expected output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}


# YOUR CODE HERE:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

combined = set1 | set2
common = set1 & set2
difference = set1 - set2

print(combined)  # all unique items
print(common)  # common items
print(difference)


# ============================================================================
# EXERCISE 11: Dictionary Basics
print("\n" + "=" * 60)
print("EXERCISE 11: Dictionary Basics")
print("=" * 60)
# ============================================================================
# Create a dictionary for a student:
# student = {"name": "Alice", "age": 20, "grade": "A"}
# Add a new key "city" with value "Stockholm"
# Update the "age" to 21
# Print the dictionary
# Expected output: {'name': 'Alice', 'age': 21, 'grade': 'A', 'city': 'Stockholm'}


# YOUR CODE HERE:
student = {"name": "Alice", "age": 20, "grade": "A"}
student.update(city="Stockholm")
student.update(age=21)

print(student)


# ============================================================================
# EXERCISE 12: Dictionary Iteration
print("\n" + "=" * 60)
print("EXERCISE 12: Dictionary Iteration")
print("=" * 60)
# ============================================================================
# Create a dictionary: prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}
# Loop through and print each item and its price in format:
# "apple costs 1.5"
# Expected output:
# apple costs 1.5
# banana costs 0.5
# cherry costs 2.0


# YOUR CODE HERE:
prices = {"apple": 1.5, "banana": 0.5, "cherry": 2.0}

for product, price in prices.items():
    print(f"{product} costs {price}")


# ============================================================================
# EXERCISE 13: Most Frequent Character
print("\n" + "=" * 60)
print("EXERCISE 13: Most Frequent Character")
print("=" * 60)
# ============================================================================
# Given: sentence = "This is a common interview question"
# Write code to find the most repeated character (ignore spaces)
# Hint: Use a dictionary to count characters, then find the max
# Print the character and its count
# Expected output: i: 5


# YOUR CODE HERE:
sentence = "This is a common interview question"
sentence = sentence.lower()

counter = {}

for char in sentence:
    if char != " ":
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

most_frequent_char = max(counter, key=counter.get)  # type: ignore

print(f"{most_frequent_char}: {counter.get(most_frequent_char)}")
