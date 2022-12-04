f=open('04/input.txt','r')
l=f.read().split("\n")
le=[[list(map(int,y.split("-"))) for y in x.split(",")] for x in l]
c=0
for e in le:
    di1=e[0][0]-e[1][1]
    di2=e[0][1]-e[1][0]
    di=di1*di2
    if di<=0:
        c+=1
print(c)