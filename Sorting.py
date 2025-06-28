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
        if num1[d] > num1[d+1]:
            temp = num1[d]
            num1[d] = num1[d + 1]
            num1[d+1] = temp
print(num1)

#insertion sort
num2 = [6,7,3,2,4,5,8,0,9,10,1]
for i in range(1, 11):
    num = num2[i]
    j = i - 1
    while j >= 0 and num < num2[j]:
        num2[j+1] = num2[j]
        j = j - 1
    num2[j+1] = num
print(num2)
