
while(True):
    n=int(input())
    if n==0:
        break
    l=list(input())
    mini = 2000005
    d=0
    r=0
    flagr=False
    flagd=False
    if "Z" in l:
        print("0")
    else:
        for i in range(n):
            if l[i] == "R":
                r=i
                flagr=True
                if flagd:
                    mini=min(mini,abs(r -d))

            elif l[i] == "D":
                d=i
                flagd=True
                if flagr:
                    mini = min(mini, abs(r - d))
        print(mini)
