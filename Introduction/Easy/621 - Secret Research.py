t=int(input())
for _ in range(t):
    s=input()
    if int(s)==1 or int(s)==4 or int(s)==78:
        print("+")
    elif s[-1]=="5" and s[-2]=="3":
        print("-")
    elif s[-1]=="4" and s[0]=="9":
        print("*")
    elif s[0]=="1" and s[1]=="9" or s[2]=="0":
        print("?")
    else:
        pass
