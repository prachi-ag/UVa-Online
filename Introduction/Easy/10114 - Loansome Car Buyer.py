l=[0 for i in range(101)]
while(True):
    loanDur , downPayment , loan , nRec=map(float,input().split())
    if loanDur<0:
        break
    for _ in range(int(nRec)):
        m,p=map(float,input().split())
        for i in range(int(m),101):
            l[i]=p
    monthlyPayment = loan / loanDur
    curVal = (loan + downPayment) * (1 - l[0])
    curLoan = loan
    c = 0
    while (curVal < curLoan):
        c+=1
        curLoan -= monthlyPayment
        curVal = curVal * (1-l[c])
    if c==1:
        print("1 month")
    else:
        print(c,"months")
