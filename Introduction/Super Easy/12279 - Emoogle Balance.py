k=1
while(True):
    s=int(input())
    if s==0:
        break
    l=list(map(int,input().split()))
    z=l.count(0)
    n=s-z
    print("Case",str(k)+":",n-z)
    k=k+1
