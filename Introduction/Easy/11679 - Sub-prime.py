while(True):
    bankMoney=[0 for i in range(22)]
    bank,debentures=map(int,input().split())
    if bank==0 and debentures==0:
        break
    flag=0
    l=list(map(int,input().split()))
    for j in range(len(l)):
        bankMoney[j]=l[j]
    for i in range(debentures):
        d,c,v=map(int,input().split())
        bankMoney[d-1]-=v
        bankMoney[c-1]+=v

    for i in range(bank):
        if bankMoney[i]<0:
            flag=1
            break

    if flag==1:
        print("N")
    else:
        print("S")
