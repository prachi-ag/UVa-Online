t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x<y:
        print("<")
    elif x>y:
        print(">")
    else:
        print("=")
