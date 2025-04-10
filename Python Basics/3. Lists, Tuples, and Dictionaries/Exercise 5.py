# Sort a list of random numbers without using .sort().

list_num = [2,3,4,6,1,9,7]
print("Original List:", list_num)

for i in range(0, len(list_num)):
    for j in range(i + 1, len(list_num)):
        if list_num[i] >= list_num[j]:
            list_num[i], list_num[j] = list_num[j],list_num[i]


print("Sorted List:  ", list_num)