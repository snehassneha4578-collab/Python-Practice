set1={'Ram','Shyam','Jenny'}
set2={'Jenny','Jiya','Aakash'}
print(set1.isdisjoint(set2))
print(set1)
del set2
set2={'Jiya','Aakash'}
print(set1.isdisjoint(['Moha','Shiva']))
print(set1.isdisjoint(['Moha','Shiva','Jenny']))
print(set1.issubset(['Moha','Shiva','Jenny']))
print(set1<=set1)
print(set1>=set1)
print(set1==set2)
print(set1.issuperset(set2))
print(set2.issuperset(set1))
print(set1<=set2)
print(set1>=set2)
print(set1,set2)
set2.clear()
print(set2)
del set2


