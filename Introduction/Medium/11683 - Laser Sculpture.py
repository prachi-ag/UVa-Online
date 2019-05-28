
while(True):
    j=list(map(int,input().split()))
    if len(j)==1:
        break
    h=j[0]
    c=j[1]
    l=list(map(int,input().split()))

    k=0
    k=k+h-l[0]
    for i in range(1,c):
        if (l[i] != h):
            temp = l[i - 1] - l[i]
            if (temp > 0):
                k += temp
    print(k)
        
