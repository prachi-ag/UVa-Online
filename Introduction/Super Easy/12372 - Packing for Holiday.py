t=int(input())
k=1
for _ in range(t):
    s = list(map(int, input().split()))
    if all(x <= 20 for x in s):
        print("Case", str(k) + ":", "good")
        k = k + 1
    else:
        print("Case", str(k) + ":", "bad")
        k = k + 1
