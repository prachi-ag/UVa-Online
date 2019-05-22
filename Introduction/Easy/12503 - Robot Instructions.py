t=int(input())
for _ in range(t):
    n = int(input())
    l=[0 for i in range(n)]
    for i in range(n):
        s = list(map(str, input().split()))
        if s[0]=="LEFT":
            l[i]=-1
        elif s[0]=="RIGHT":
            l[i]=1
        else:
            l[i]=l[int(s[2])-1]
    print(sum(l))
