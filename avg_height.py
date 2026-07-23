height=input("Enter all height separated by space:")
height_list=height.split()
count=0
for i in height_list:
    count+=1
print(count)
for i in range(0,count):
    height_list[i]=int(height_list[i])
print(height_list)

for i in range(count):
    height_list[i]=int(height_list[i])
sum=0
for person in height_list:
    sum+=person
total=0

for person in height_list:
    total+=person
avg=total/count
print(avg)