list1 = [1,2,3,4,5,6,7]

list_result = []

for i in list1:
    list_result.append(i)
    if i % 2 == 0:
        i *=2
        list_result.append(i)

print(list_result)