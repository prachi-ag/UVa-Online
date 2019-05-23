song = ["Happy", "birthday", "to", "you", "Happy", "birthday", "to", "you", "Happy", "birthday", "to", "Rujia", "Happy", "birthday", "to", "you"]
n=int(input())
name=[]
for i in range(n):
    name.append(input())
i=0
j=0
flag=0
while(True):
    print(name[i]+":",song[j])
    if i==n-1:
        flag=1
    if flag==1 and j==15:
        break
    i=i+1
    j=j+1
    if i>=n:
        i=0
    if j>=16:
        j=0
