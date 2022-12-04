f=open('04/input.txt','r')
l=f.read().split("\n")
le=[[list(map(int,y.split("-"))) for y in x.split(",")] for x in l]
c=0
for e in le:
    dg=e[0][0]-e[1][0]
    dd=e[0][1]-e[1][1]
    d=dg*dd
    if d<=0:
        c+=1
print(c)