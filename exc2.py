l1: list[int] = []
l2: list[int] = []
sentinel:int = -999

while True:
    num: int = int(input("enter a number: "))
    if num == sentinel:
        break
    elif 0 <= num <= 10:
        l1.append(num)
        for i in range (11):
            if l1.count(i) > 0:
                print (f"[{i}]: {l1.count(i)}", end = " ")
        print ()
    else:
        continue
print (l1) #-- to check


for j in range (11):
    l2.insert(j,l1.count(j))
print (l2)

