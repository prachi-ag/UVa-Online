t=int(input())
k=0
for _ in range(t):
    k+=1
    mile=0
    juice=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in l:
        mile+=(1+i//30)*10
        juice+=(1+i//60)*15

    if mile<juice:
        print("Case",str(k)+":","Mile",mile)
    elif mile>juice:
        print("Case",str(k)+":","Juice",juice)
    else:
        print("Case",str(k)+":","Mile Juice",juice)
