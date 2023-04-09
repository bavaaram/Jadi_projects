n = 10
nums = list()
for i in range(n + 1)
    if (i % 3 == 0) or (i % 5 == 0):
        nums.append(i)
    else:
        continue
summ = 0
for j in nums:
    summ = summ + j

print(summ)


