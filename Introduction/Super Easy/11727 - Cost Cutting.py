k=1
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    l.sort()
    print("Case",str(k)+":",l[1])
    k=k+1

