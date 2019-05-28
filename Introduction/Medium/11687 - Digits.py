
while(True):
    n=(input())
    if n=="END":
        break
    c=1
    while(n!='1'):
        n=str(len(n))
        c=c+1
    print(c)
