opening = ["{", "[", "("]
closing = ["}", "]", ")"]

q = input("Which expression do you want?")
print(q)

from Stack import Stack

brackets = Stack(10)
for i in q:
    if i in opening:
        brackets.push(i)
    elif i in closing:
        index = closing.index(i)
        b = opening[index]
        if len(brackets.stack) != 0 and brackets.top() == b:
            brackets.pop()
if len(brackets.stack) == 0:
    print("Brackets match!")
else:
    print("Brackets do not match :(")