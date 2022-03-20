c = []
a = []
b = []
N = int(input())
aa = input().strip().split(" ")


print(aa)
for i in aa:
    # aa =int(input().split(" "))
    if i == " ":
        continue

    a.append(int(i))
print(a)
aa = input().strip().split(" ")

for i in aa:
    if i == " ":
        continue
    # aa =int(input().split(" "))
    b.append(int(i))

ele_start = -1
ele_end = -1
for i in a:
    if i in b:
        continue
    else:
        ele_start = i

for i in b:
    if i in a:
        continue
    else:
        ele_end = i
c.append(ele_start)
index = ele_start
for i in range(len(a)):
    index = a.index(index)
    c.append(b[index])
    if b[index] == ele_end:
        break
    else:
        index = b[index]
if len(c) != len(a) + 1:
    print(-1)
else:
    # print(c)
    for i in c :
        print(i,sep=
              ' ')
