#The answer is "LOOP" if there is more than 1 piece and the number of
#M is equal to the number of F. 

 
t=int(input())
for _ in range(t):
    c=0
    l=list(map(str,input().split()))
    s="".join(l)
    m=s.count("M")
    f=s.count("F")
    if len(l)>1 and m==f:
        print("LOOP")
    else:
        print("NO LOOP")

