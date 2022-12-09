f=open('08/input.txt','r').read()
l=f.split("\n")
forest=[]
for c in l:
    forest.append(list(map(int,c)))
print('hello')


def check_higher(forest,x,y):
    h=forest[x][y] #Get reference height
    hx=len(forest)
    hy=len(forest[x])
    (a,b,c,d)=(0,0,0,0)
    (s,t,u,v)=(0,0,0,0)
    for i in range(x-1,-1,-1):#check haut
        if forest[i][y]>=s:
            a=x-i
            s=forest[i][y]
    for i in range(x+1,hx): #Check bas
        if forest[i][y]>=t: 
            b=i-x
            t=forest[i][y]
    for j in range(y-1,-1,-1): #Check gauche
        if forest[x][j]>=u: 
            c=y-j
            u=forest[x][j]
    for j in range(y+1,hy): #Check droite
        if forest[x][j]>=v: 
            d=j-y
            v=forest[x][j]
    return (a,b,c,d),(s,t,u,v)


from math import prod
print(check_higher(forest,3,2),prod(check_higher(forest,3,2)[0]))


c=0
hx=len(forest)
hy=len(forest[0])
for x in range(hx):
    for y in range(hy):
        sc=prod(check_higher(forest,x,y)[0])
        if sc>c: 
            c=sc
            print(check_higher(forest,x,y),sc,forest[x][y],x,y)
print (c)
