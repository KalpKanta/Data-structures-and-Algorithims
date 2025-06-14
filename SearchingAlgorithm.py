n = [1,2,3,4,5,6,5,5,5,5,5,7,8,5,9,10]

#Linear search:
i = int(input("What value are you looking for?: "))
search = False
x = 0

for d in n:
    if d == i:
        search = True
        x = x + 1
if search == True:
    print("Number is present", x, "times")
else:
    print("Your nuber is not present in the list.")

#Binary search:
num = [5,7,6,8,9,10,13,11,12,14,15]
num.sort()
l = 0
h = 10
number = int(input("What number do you watn to see if its the middle number?"))
while l <= h:
    mid = (l + h)//2
    num1 = num[mid]
    if num1 == number:
        search = True
        break
    elif number < num1:
        h = mid - 1
    elif number > num1:
        l = mid + 1