cp1 = 0
cp2 = 0
for i in range(6):
    p1 = int(input("enter"))
    p2 = int(input("enter"))
    if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2)  :
        cp1 += 1
    elif (p1 == 3 and p2 == 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 3)  :
        cp2 += 1
    else:
        continue
if cp1 == cp2:
    print("draw!!")
elif cp1 > cp2:
    print("p1 win")
elif cp1 < cp2:
    print("p2 win")