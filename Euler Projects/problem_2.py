fibo = list()
fibo.append(1)
fibo.append(2)
i = 1
summ = 0
while fibo[i] < 4000000:
    fibo.append(fibo[i] + fibo[i - 1])
    i += 1

for j in fibo:
    if j % 2 == 0:
        summ = summ + j

print(summ)

