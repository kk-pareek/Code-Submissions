x1, v1, x2, v2 = 0, 3, 4, 2
i = 1
while i in range(10001):
    x = max(x1, x2)
    y = min(x1, x2)
    v = max(v1, v2)
    w = min(v1, v2)
    x1 += v1
    x2 += v2
    if x > y and v >= w:
        result = 'NO'
    elif x1==x2 and (v >= w):
        result = 'YES'
    else:
        result = 'YES'
    print(i, result, end= '')
    i+=1