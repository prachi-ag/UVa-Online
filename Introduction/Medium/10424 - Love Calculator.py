def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
lowercase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while(True):
        z1=0
        z2=0
        try:
            s1 = input()
            s2 = input()
        except EOFError:
            break
        for i in s1:
            i=i.lower()
            if i in lowercase:
                z1+=lowercase.index(i)+1
        while (len(str(z1)) > 1):
            z1 = sumDigits(z1)

        for i in s2:
            i = i.lower()
            if i in lowercase:
                z2 += lowercase.index(i) + 1
        while (len(str(z2)) > 1):
            z2 = sumDigits(z2)
        if z1>=z2:
            print("{:.2f}".format((z2/z1)*100),"%")
        else:
            print("{:.2f}".format((z1 / z2) * 100),"%")
