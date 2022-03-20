
def fun(n):
    fac_list = []
    x = 1
    fac_list.append(x)
    x += 1
    index = 0
    while (fac_list[index] <= n):
        var = fac_list[index] * x
        fac_list.append(var)
        x += 1
        index += 1
    xz=0
    if n in fac_list:
        print(1)
        return
    fac_list.sort(reverse=True)
    count = 0
    for i in fac_list:
        if n%i == 0:
            count += n%i
            print(count)
            return
        else :
            count += n%i
            n -= n/

