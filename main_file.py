print("Put numbers: ")
posled = [float(i) for i in input().split()]
le = len(posled) - 1
check = True
if len(posled) > 1:
    posled2 = []
    for i in range(len(posled)):
        if posled[i] < 0:
            posled2.append(posled[i])
    if len(posled2) == len(posled):
        posled.sort()
    else:
        posled.sort(key=abs)
    q = posled[1]/posled[0]
    print("q = ", q)
    posled.sort(key=abs)
    print("Sorted progression: ", posled)
elif not posled:
    print("List is empty!")

elif len(posled) == 1:
    print("The progression is too small")

for i in range(0, le):
    chislo1 = posled[i] # запись в переменные элемент массива и следющий элемент после него
    chislo2 = posled[i+1]
    if chislo2 / chislo1 != q:
        check = False
        break
if check:
    print("This is a geometric progression!")
    if q < 1 and q > 0:
        print("Progression is decreasing")
    elif q < 0:
        print("Sign-alternating progression")
else:
    print("This is not a geometric progression!")
