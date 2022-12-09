f=open('08/input.txt','r').read()
l=f.split("\n")
forest=[]
for c in l:
    forest.append(list(c))

def check_higher(forest,x,y):
    h=forest[x][y] #Get reference height
    hx=len(forest)
    hy=len(forest[x])
    (a,b,c,d)=(1,1,1,1)
    for i in range(x):#check haut
        if forest[i][y]>=h: a=0
    for i in range(x+1,hx): #Check bas
        if forest[i][y]>=h: b=0
    for j in range(y): #Check gauche
        if forest[x][j]>=h: c=0
    for j in range(y+1,hy): #Check dorite
        if forest[x][j]>=h: d=0
    return (a,b,c,d)

c=0
hx=len(forest)
hy=len(forest[0])
for x in range(hx):
    for y in range(hy):
        if max(check_higher(forest,x,y))==1: c+=1
print (c)