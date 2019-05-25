while(True):

    n=int(input())
    if n==0:
        break
    l=list(map(str,input().split()))
    dir=0
    for i in l:
        if i=="No":
            continue
        if i=="+z":
            if dir==0:
                dir=4
            elif dir==1:
                dir=5
            elif dir==4:
                dir=1
            elif dir==5:
                dir=0
        elif i=="-z":
            if (dir == 0):
                dir = 5
            elif (dir == 1):
                dir = 4
            elif (dir == 4):
                dir = 0
            elif dir == 5:
                dir = 1

        elif i=="+y":
            if (dir == 0):
                dir = 2
            elif (dir == 1):
                dir = 3
            elif (dir == 2):
                dir = 1
            elif (dir == 3):
                dir = 0
        elif i=="-y":
            if (dir == 0):
                dir = 3
            elif (dir == 1):
                dir = 2
            elif (dir == 2):
                dir = 0
            elif (dir == 3):
                dir = 1
    if(dir == 0):
        print("+x")
    elif(dir == 1):
        print("-x")
    elif(dir == 2):
        print("+y")
    elif(dir == 3):
        print("-y")
    elif(dir == 4):
        print("+z")
    elif(dir == 5):
        print("-z")


