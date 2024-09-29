# exc.a
temp_list: list[float] = []
# exc.b
sentinel: float = -999
while True:
    temp: float = float(input("enter temp: "))
    if temp == sentinel:
        break
    elif -50 < temp < 50:
        temp_list.append(temp)
# print (temp_list) -- to check
# exc.c
temp_list.extend([-20, 39.1, 18.5])
# print(f"extended: {temp_list}") -- to check
# exc.d
# extend changes the current list while, (+) creates a new list
# exc.e
print(f" the highest temp is: {max(temp_list)}")
print(f" the lowest temp is: {min(temp_list)}")
# exc.f
print(18.5 in temp_list)
# exc.g
print(temp_list.count(-20))
# exc.h
if len(temp_list) != 0:
    print(sum(temp_list) / len(temp_list))
# exc.i
for temp in temp_list:
    print(temp)
# exc.j
print(temp_list.index(39.1))
# exc.k
del temp_list[0]
print(temp_list)
# exc.l
del temp_list[0::2]
print(temp_list)
# exc.m
if 18.5 in temp_list:
    temp_list.remove(18.5)
    print("18.5 was removed from the list")
else:
    print("18.5 is not in the ,list")
# if we didn't check if 18.5 was in the list and it wasn't, the program will crash because it can't remove something that is not in the list
# exc.n
temp_last: float = temp_list.pop()
# print (temp_last) -- to check
# exc.o
new_list: list[float] = temp_list.copy()
new_list.sort()
# print (temp_list) -- to check
# print(new_list) -- to check
# exc.p
new_list2: list[float] = temp_list.copy()
new_list2.sort(reverse=True)
# print (new_list2) -- to check
