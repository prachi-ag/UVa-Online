

while(True):
    current,goto=map(int,input().split())
    if current==-1 or goto==-1:
        break
    else:
        if current > goto:
            one = current - goto
            two = goto + 100 - current

        else:

            one = goto - current
            two = current + 100 - goto
    print(min(one,two))
