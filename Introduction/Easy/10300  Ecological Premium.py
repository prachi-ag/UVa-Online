t=int(input())
for _ in range(t):
    s=0
    n=int(input())
    for i in range(n):
        a,b,c=map(int,input().split())
        s=s+a*c
    print(s)
