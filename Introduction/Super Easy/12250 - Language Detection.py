i=0
while(True):
    i+=1
    s=input()
    if s=="#":
        break
    else:
        if s == 'HELLO':
            print('Case %d:' % i, 'ENGLISH')
        elif s == 'HOLA':
            print('Case %d:' % i, 'SPANISH')
        elif s == 'HALLO':
            print('Case %d:' % i, 'GERMAN')
        elif s == 'BONJOUR':
            print('Case %d:' % i, 'FRENCH')
        elif s == 'CIAO':
            print('Case %d:' % i, 'ITALIAN')
        elif s == 'ZDRAVSTVUJTE':
            print('Case %d:' % i, 'RUSSIAN')
        else:
            print('Case %d:' % i, 'UNKNOWN')
