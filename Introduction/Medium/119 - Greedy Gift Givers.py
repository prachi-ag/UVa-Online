

while(True):
    try:
        n = int(input())
    except EOFError:
        break

    l=list(map(str,input().split()))
    net=[0 for i in range(n)]
    for i in range(n):
        q=list(map(str,input().split()))
        if q[2]!="0":
            net[l.index(q[0])]-=(int(q[1])-int(q[1])%int(q[2]))
            amt=((int(q[1])-int(q[1])%int(q[2]))//int(q[2]))
            for j in range(int(q[2])):
                net[l.index(q[3+j])]+=amt
    for i in range(n):
        print(l[i],net[i])
    print()

