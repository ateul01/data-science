def fun(arr):
    m = 1
    flag = False
    for x in arr:
        print(x,m)
        if x!=0:
            m*=x
        elif flag == True:
            return [0]*len(arr)
        else:
            flag = True
    ans = []
    if flag:
        for x in arr:
            if x!=0:
                ans.append(0)
            else:
                ans.append(m)
    else:
        for x in arr:
            ans.append(int(m/x))
    return ans
print(fun(list(map(int,input().split()))))
