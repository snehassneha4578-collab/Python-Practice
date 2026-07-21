set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Aakash'}

print(set1.union(set2))
print(set1 | set2)

set3 = {'Ankur', 'Pradeep'}

print(set1.union(set2, set3))
print(set1.union(('Mohan', 'Jenny')))

print(set1 | {'Mohan', 'Jenny'})

set1.update(set2)
print(set1)

set1 |= set2
print(set1)

print(set1.intersection(set2))
print(set1.intersection(set2, set3))

set1.intersection_update(set2)
print(set1)

print(set1.symmetric_difference(set2))
print(set1)

set1.symmetric_difference_update(set2)
print(set1)

set3 = {'Ankur', 'Pradeep', 'Ram'}

print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))

set1.symmetric_difference(set2)
print(set1)