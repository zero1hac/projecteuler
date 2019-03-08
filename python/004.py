max = 0
high = 999
low = 99
for i in range(high, low, -1):
    for j in range(high, low, -1):
        res = j*i
        if str(res) == str(res)[::-1] and res > max:
            max = res
print(max)
