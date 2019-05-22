t=int(input())
k=0
for _ in range(t):
    k=k+1
    n=int(input())
    l=list(map(int,input().split()))
    high=0
    low=0
    for i in range(len(l)-1):
        if l[i+1]>l[i]:
            low+=1
        elif l[i+1]<l[i]:
            high+=1
    print("Case",str(k)+":",low,high)
