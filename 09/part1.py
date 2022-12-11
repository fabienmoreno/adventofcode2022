


def next_tail(hpos,tpos):
    split=(hpos[0]-tpos[0],hpos[1]-tpos[1])
    if split==(0,0):
        ntpos=tpos
    elif max(map(abs,split))==1:
        ntpos=tpos
    else:
        dict_move={(1,2):(1,1), (2,1):(1,1), (-1,2):(-1,1), (1, -2):(1,-1), (-2,-1):(-1,-1), (-2,1):(-1,1), (-1,-2):(-1,-1), (2,-1):(1,-1),
        (2,0):(1,0),(0,2):(0,1),(0,-2):(0,-1),(-2,0):(-1,0)}
        move=dict_move[split]
        ntpos=(move[0]+tpos[0],move[1]+tpos[1])
    return ntpos

f=open('09/input.txt','r')
l=f.read().split("\n")

hpos=(0,0)
tpos=(0,0)
tset=set()
tset.add(tpos)

for c in l:
    com=c.split(" ")
    iter=int(com[1])
    dir_dict={"R":(1,0), "L": (-1,0), "U":(0,1), "D":(0,-1)}
    dir=dir_dict[com[0]]
    count=0
    while count<iter:
        #print("Position initiale : ", hpos, tpos, "mouvement :", dir)
        nhpos=(hpos[0]+dir[0],hpos[1]+dir[1])
        ntpos=next_tail(nhpos,tpos)
        hpos=nhpos
        tpos=ntpos
        #print("Position finale : ", hpos,tpos)
        tset.add(tpos)
        count+=1

print("Number of different tail position: ", len(tset))


"""
    elif hpos[0]==tpos[0]:
        if hpos[1]>tpos[1]:
            ntpos=(tpos[0],tpos[1]+1)
        if hpos[1]<tpos[1]:
            ntpos=(tpos[0],tpos[1]-1)
    elif hpos[1]==tpos[1]:
        if hpos[0]>tpos[0]:
            ntpos=(tpos[0]+1,tpos[1])
        if hpos[0]<tpos[0]:
            ntpos=(tpos[0]-1,tpos[1])
    else:
        split=(hpos[0]-tpos[0],hpos[1]-tpos[1])"""