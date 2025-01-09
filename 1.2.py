inputs = [i for i in input().split()]

summ=0
for i in inputs:
    summ+=int(i)
mean = summ/len(inputs)

temp_list=inputs
temp_list.sort()
mid = len(temp_list) // 2
res = (int(temp_list[mid]) + int(temp_list[~mid])) / 2

mode =max(set(inputs), key=inputs.count)

print(f"The mode is {mode}")
print(f"The mean is {mean}")
print(f"The median is {res}")
