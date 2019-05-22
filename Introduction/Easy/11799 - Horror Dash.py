t=int(input())
k=0
for _ in range(t):
    k=k+1
    l=list(map(int,input().split()))
    l=l[1:]
    print("Case",str(k)+":",max(l))
