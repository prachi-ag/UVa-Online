t=int(input())
print("Lumberjacks:")
for _ in range(t):
    l=list(map(int,input().split()))
    k=l.copy()
    l.sort()
    ascending=l.copy()
    descending=list(reversed(l))
    if k==ascending or k==descending:
        print("Ordered")
    else:
        print("Unordered")
