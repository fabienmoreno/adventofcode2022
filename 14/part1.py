f=open('14/simple_perso.txt','r').read()
l=f.split("\n")

y_max=50
x_max=15
m_zero=[[0 for count in range(y_max)] for count in range(x_max)]


def draw(m):
    f=open("14/matrix.txt",'w')
    for y in range(y_max):
        for x in range(x_max):
            if m[x][y]==1: f.write("#")
            else: f.write(".")
        f.write('\n')
    f.close()     


#Draw line of rock
for seg in l:
    cords=seg.split(" -> ")
    seg_t=[]
    for cord in cords:
        res = tuple(map(int, cord.split(',')))
        seg_t.append(res)
    for i in range(len(seg_t)-1):
        sx=seg_t[i][0]
        sy=seg_t[i][1]
        ex=seg_t[i+1][0]
        ey=seg_t[i+1][1]
        if sx==ex: #Iterate on Y
            #print("Iterate y : ", sx, range(min(sy,ey),max(sy,ey)+1))
            for y in range(min(sy,ey),max(sy,ey)+1):
                m_zero[sx][y]=1
        elif sy==ey: #Iterate on X
            #print("Iretage X : ", sy, range(min(sx,ex),max(sx,ex)+1))
            for x in range(min(sx,ex),max(sx,ex)+1):
                m_zero[x][sy]=1
        else:
            raise Exception("Error line rock break")


def find_drop(ic):
    #print(ic)
    if m_zero[ic[0]][ic[1]]==1:
        draw(m_zero)
        raise Exception('Satruration')
    else:
        if m_zero[ic[0]][ic[1]+1]==0: #Void below
            #print("Void below")
            final_cord=find_drop((ic[0],ic[1]+1))
        elif m_zero[ic[0]][ic[1]+1]==1:
            if m_zero[ic[0]-1][ic[1]+1]==0:
                final_cord = (ic[0]-1,ic[1]+1)
                #print("Go left")
            elif m_zero[ic[0]+1][ic[1]+1]==0:
                final_cord=(ic[0]+1,ic[1]+1)
                #print("Go right")
            else: 
                final_cord=(ic[0],ic[1])
                #print("Stack")
    #print(final_cord)
    return final_cord

"""init_cord = (500,0)
final_cord = find_drop(init_cord)
print(final_cord)"""
i=0
while True:
    init_cord = (10,0)
    final_cord = find_drop(init_cord)
    m_zero [final_cord[0]][final_cord[1]]=1
    print(i, final_cord)
    i+=1