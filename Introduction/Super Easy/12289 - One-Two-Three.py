t=int(input())
one=set("one")
two=set("two")
for _ in range(t):
    s=list(input())
    if len(s)==5:
        print("3")
    elif ((s[0] == 't' and s[1] == 'w') or (s[0] == 't' and s[2] == 'o') or (s[1] == 'w' and s[2] == 'o')):
        print("2")
    else:
        print("1")
