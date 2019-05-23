g=0
while(True):
    g=g+1
    n,m,c=map(int,input().split())
    if n==0 and m==0 and c==0:
        break

    cap=[0 for i in range(n)]
    power=[0 for i in range(m)]
    flag=[0 for i in range(n)]
    net=0
    max=0
    for i in range(n):
        cap[i]=int(input())
    for i in range(m):
        power[i]=int(input())
    for i in power:
        if flag[i-1]==0:
            net+=cap[i-1]
            flag[i-1]=1
        else:
            net -= cap[i - 1]
            flag[i-1]=0
        if net > max:
            max = net
    if max<=c:
        print("Sequence", g)
        print("Fuse was not blown.")
        print("Maximal power consumption was",max,"amperes.")
        print()
    else:
        print("Sequence", g)
        print("Fuse was blown.")
        print()
