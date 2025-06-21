#selection sorting
num = [6,7,2,4,10,0,9,1,3,8,5]

for i in range(10):
    s = num[i]
    p = i
    for d in range(i + 1, 11):
        c = num[d]
        if c < s:
            s = c
            p = d

    temp = num[i]
    num[i] = s
    num[p] = temp
print(num)



#bubble sort
num1 = [6,7,1,4,2,3,5,9,8,10]

for i in range(10):
    for d in range(0, 10-i-1):
        if num1[d] num1[d+1]