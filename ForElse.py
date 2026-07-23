tuple1=(2,56,34,3,5,-1)
for i in tuple1:
    print(i)
else:
    print("Loop Successfully Completed and we are in else block now")
for i in tuple1:
    print(i)
    if i==5:
        break
for i in tuple1:
    if i%6==0:
        print(i)
        break
    else:
        print("There is no number divisible by 6")
for i in tuple1:
    if i%6==0:
        print(i)
        break
else:
    print("There is no number divisible by 6")