k=0
t=int(input())
for _ in range(t):
    k+=1
    l=[]
    j=[]
    for i in range(10):
        s=list(map(str,input().split()))
        s[1]=int(s[1])
        j.append(s[1])
        l.append(s)
    ans=sorted(l, key=lambda x: x[1])
    c=j.count(max(j))
    print("Case","#"+str(k)+":")
    for i in range(c):
        print(ans[len(ans)-c+i][0])
