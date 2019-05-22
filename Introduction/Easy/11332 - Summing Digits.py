def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
while(True):
    n=int(input())
    if n==0:
        break
    else:
        while(len(str(n))>1):
            n=sumDigits(n)
    print(n)
