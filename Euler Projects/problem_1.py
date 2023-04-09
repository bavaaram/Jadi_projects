n = 1000
nums = list()
for i in range(n):
    if (i % 3 == 0) or (i % 5 == 0):
        nums.append(i)
    else:
        continue
summ = 0
for j in nums:
    summ = summ + j

print(summ)


