set1 = {10, 56, 89, 90, 'Sneha', True}
print(set1)

set2 = {10, 56, 89, 'jenny', True, 10}
print(type(set1))
print(type(set2))

set1.add(99)
print(set1)

print(len(set1))

set1.discard(68)      # No error if element doesn't exist
print(set1)

set1.clear()
print(set1)

# Add a tuple instead of a list
set1.add((13, 14, 15))
print(set1)