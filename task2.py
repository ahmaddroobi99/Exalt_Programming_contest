
def equ(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]%l[j] == l[j]-1):
                print(l[i], end=" ")
                print(l[j] , end=" ")
                print("")
                return

n = int(input())

lis = []

# print(n)
for ii in range(n+1):
    n2 = int(input())
    aal = input().strip().split(" ")
    for jj in aal:
        lis.append(int(jj))
    # print(lis)
    equ(lis)
    lis=[]

