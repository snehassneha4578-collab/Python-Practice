
# Python Day 6 - List Operations

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three:", numbers[:3])
print("Reversed:", numbers[::-1])

# Modify an element
numbers[1] = 99
print("Modified:", numbers)

# Add elements
numbers.append(60)
numbers.extend([70, 80])
numbers.insert(1, 15)
print("After adding:", numbers)

# Remove elements
numbers.remove(30)
removed = numbers.pop()
print("Removed element:", removed)
print("After removing:", numbers)

# Search and count
print("Is 40 present?", 40 in numbers)
print("Count of 10:", numbers.count(10))

# Sorting
numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

# Copy a list
copied = numbers.copy()
copied.append(100)
print("Original:", numbers)
print("Copied:", copied)

# Nested list
matrix = [[1, 2, 3], [4, 5, 6]]
print("Matrix:", matrix)
print("Nested element:", matrix[1][2])

# Clear a list
temporary = [1, 2, 3]
temporary.clear()
print("Cleared list:", temporary)

print("Python Day 6 completed!")
