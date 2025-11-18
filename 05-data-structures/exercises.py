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
# Expected output: i: 6


# YOUR CODE HERE:


# ============================================================================
# EXERCISE 14: Dictionary Comprehension
print("\n" + "=" * 60)
print("EXERCISE 14: Dictionary Comprehension")
print("=" * 60)
# ============================================================================
# Create a dictionary comprehension that maps numbers 1-5 to their cubes
# Expected output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


# YOUR CODE HERE:


# ============================================================================
# EXERCISE 15: Unpacking Operator
print("\n" + "=" * 60)
print("EXERCISE 15: Unpacking Operator")
print("=" * 60)
# ============================================================================
# Create two lists:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Use the unpacking operator to combine them into one list
# Print the combined list
# Expected output: [1, 2, 3, 4, 5, 6]


# YOUR CODE HERE:


print("\n✅ Exercises complete! Run the program to test your solutions.")
