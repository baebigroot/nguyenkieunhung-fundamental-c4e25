num = [-19, -17, -11, 11, 15, 12, -10]
min_num = 999999
for index, i in enumerate(num):
    if min_num > i:
        min_num = i
        min_index = index

print(min_num)
print(min_index)

