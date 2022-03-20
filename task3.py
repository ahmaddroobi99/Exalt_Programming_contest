def fun(n , lis:list):
    sum=0
    count=0

    lis.sort(reverse=True)
    while (lis.count(-1) != len(lis)):
        if len(lis)==0 :
            break

        for i in range(len(lis)) :

            if lis[i] == -1:
                continue
            elif sum+lis[i] <= n:
                sum+=lis[i]
                lis[i] = -1
        sum =0
        count+=1
    print(count)

arr=[]
a = 0
b = 0
n = int(input())
for i in range(n):
    num = input().strip().split(" ")
    a = int(num[1])

    num2 = input().strip().split(" ")

    for j in num2:
        arr.append(int(j))

    fun(a,arr)


