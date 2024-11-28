#1.you have been given a python list [10,501,22,37,100,999,87,351] your task is to create two list one which have all the even numbers and another list which will have all the ODD numbers in it?

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the list and categorize each number
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Display the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#2.given a python list[10,501,22,37,100,999,87,351] your task is to count all the prime numbers and create a new python list which will contain all the prime numbers in it?
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create a new list to store prime numbers
prime_numbers = []

# Check each number in the list and add to prime_numbers if it's prime
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)

# Count the number of prime numbers
prime_count = len(prime_numbers)

# Display the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)
#3. given a python list [10,501,22,37,100,999,87,351] find out how many numbers are there in the given python list which are happy numbers?
def is_happy_number(n):
    seen = set()  # To track numbers we've already encountered to detect loops
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))  # Sum of squares of digits
    
    return n == 1

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count how many numbers are happy numbers
happy_numbers = [num for num in numbers if is_happy_number(num)]

# Display the results
print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", len(happy_numbers))

#4.write a python program to find the sum of the first and last digit of an integer
def sum_first_last_digit(number):
    # Convert the number to a string to easily access the first and last digits
    number_str = str(abs(number))  # We use abs() to handle negative numbers
    
    # Get the last digit (the last character of the string)
    last_digit = int(number_str[-1])
    
    # Get the first digit (the first character of the string)
    first_digit = int(number_str[0])
    
    # Return the sum of the first and last digits
    return first_digit + last_digit

# Example usage
number = 7539
result = sum_first_last_digit(number)

print(f"The sum of the first and last digit of {number} is {result}")

#3.you have been given a list of N integers which representsthe number of mangoes in a bag. each bag has a variable number of mangoes. there are M students in a guvi class, your task is to distribute the mangoes in such a way that each student gets oe bag. the difference between the number of mangoes in a bag with maximum mangoes and bag with mangoes  given to the student is minimum?

def min_mango_difference(mangoes, M):
    # Sort the list of mangoes in ascending order
    mangoes.sort()
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # We iterate over the sorted list and check the difference for each subarray of size M
    for i in range(len(mangoes) - M + 1):
        # The difference between the max and min in the current subarray
        diff = mangoes[i + M - 1] - mangoes[i]
        # Update the minimum difference
        min_diff = min(min_diff, diff)
    
    return min_diff

# Example usage
mangoes = [10, 20, 15, 40, 30, 50]
M = 3  # Number of students (i.e., number of bags to distribute)
result = min_mango_difference(mangoes, M)

print(f"The minimum difference between the bags is: {result}")

#6.you have been given three lists. your task is to find the duplicates in the three lists. write a python program for the same. you can use your own pytho list?
def find_duplicates(list1, list2, list3):
    # Convert lists to sets to remove duplicates and find common elements
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find the intersection of the three sets
    duplicates = set1.intersection(set2).intersection(set3)
    
    return list(duplicates)  # Convert the result back to a list

# Example lists
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 4, 5, 8, 9, 10]
list3 = [2, 4, 5, 6, 11, 12]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)

# Output the result
print(f"The duplicates across all three lists are: {duplicates}")

#7.from collections import Counter

def first_non_repeating(arr):
    # Count the frequency of each element in the list
    count = Counter(arr)
    
    # Iterate over the list to find the first element with frequency 1
    for num in arr:
        if count[num] == 1:
            return num
    
    # If no non-repeating element is found, return None or a message
    return None

# Example usage
arr = [4, 5, 6, 4, 7, 8, 6, 7, 9]
result = first_non_repeating(arr)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There is no non-repeating element.")


