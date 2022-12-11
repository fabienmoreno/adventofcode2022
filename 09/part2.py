def next_tail(hpos,tpos):
    split=(hpos[0]-tpos[0],hpos[1]-tpos[1])
    if split==(0,0):
        ntpos=tpos
    elif max(map(abs,split))==1:
        ntpos=tpos
    else:
        dict_move={(1,2):(1,1), (2,1):(1,1), (-1,2):(-1,1), (1, -2):(1,-1), (-2,-1):(-1,-1), (-2,1):(-1,1), (-1,-2):(-1,-1), (2,-1):(1,-1),
        (2,0):(1,0),(0,2):(0,1),(0,-2):(0,-1),(-2,0):(-1,0),
        (2,2):(1,1),(2,-2):(1,-1),(-2,2):(-1,1),(-2,-2):(-1,-1),}
        move=dict_move[split]
        ntpos=(move[0]+tpos[0],move[1]+tpos[1])
    return ntpos

f=open('09/input.txt','r')
l=f.read().split("\n")

knot_qty=10
pos_list=[(0,0) for i in range(knot_qty)]

tset=set()
tset.add(pos_list[-1])

for c in l:
    com=c.split(" ")
    iter=int(com[1])
    dir_dict={"R":(1,0), "L": (-1,0), "U":(0,1), "D":(0,-1)}
    dir=dir_dict[com[0]]
    count=0
    while count<iter:
        npos_list=pos_list
        npos_list[0]=(pos_list[0][0]+dir[0],pos_list[0][1]+dir[1])
        for i in range(1,len(npos_list)):
            npos_list[i]=next_tail(npos_list[i-1],npos_list[i])
        pos_list=npos_list
        tset.add(pos_list[-1])
        count+=1

print("Number of different tail position: ", len(tset))