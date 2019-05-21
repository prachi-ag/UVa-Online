t=int(input())
amt=0
for _ in range(t):
    l=list(map(str,input().split()))
    if len(l)==2:
        amt+=int(l[1])
    else:
        print(amt)
