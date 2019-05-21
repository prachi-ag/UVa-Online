t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=[t - s for s, t in zip(l, l[1:])]
    print(sum(x)*2)
