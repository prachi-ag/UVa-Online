f=0
while True:
    try:
        s = list(input())
    except EOFError:
        break
    for i in range(len(s)):
        if s[i] == '\"':
            if f == 0:
                s[i] = "``"
                f = 1
            else:
                s[i] = "''"
                f = 0
    print("".join(s))


