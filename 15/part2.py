f=open('15/simple.txt','r').read()
l=f.split("\n")

sensors=[]
beacons=[]

for c in l:
    c=c.replace("Sensor at x=","")
    c=c.replace(", y=",",")
    c=c.replace(": closest beacon is at x=",",")
    c=c.replace(", y",",")
    p=list(c.split(','))
    p=list(map(int, p))
    sensors.append((p[0],p[1]))
    beacons.append((p[2],p[3]))
#print(beacons)
print(sensors)

#Formule de calcul de distance taxi entre deux points 
def distance(s,b):
    d = abs(s[0]-b[0]) + abs(s[1]-b[1])
    return d

#Calculate distance for each beacon / sensor couple
distances=[]
nb_sensors=len(sensors)
for i in range(nb_sensors):
    distances.append(distance(sensors[i],beacons[i]))
print(distances)

#Calcul des coordonnée des sommets des carrés de couverture
pics=[]
for i in range(nb_sensors):
    pic=[]
    pic.append((sensors[i][0]+distances[i],sensors[i][1]))
    pic.append((sensors[i][0],sensors[i][1]+distances[i]))
    pic.append((sensors[i][0]-distances[i],sensors[i][1]))
    pic.append((sensors[i][0],sensors[i][1]-distances[i]))
    pics.append(pic)
print(pics)

#Apply a rotation on all points
def rotate(cord):
    x=cord[0]
    y=cord[1]
    n=x+y
    m=-x+y
    return(n,m)
sensors_r=[rotate(sensor) for sensor in sensors]
print(sensors_r)

pics_r=[[rotate(pic) for pic in x] for x in pics]
print("pics_r : ", pics_r)

#Calcul les plans limites dans les nouvelles coordonnées au format m_min, m_max, n_min, n_max
plans=[]
for i in range(nb_sensors):
    plan=[]
    plan.append(pics_r[i][2][0])
    plan.append(pics_r[i][0][0])
    plan.append(pics_r[i][0][1])
    plan.append(pics_r[i][1][1])
    plans.append(plan)
print("plans : ", plans)

#Définition de la zone de recherche 
x_min=0
y_min=0
x_max=20
y_max=20
## Apply rotation on zone peaks
print(rotate((x_min,y_min)),rotate((x_min,y_max)),rotate((x_max,y_min)),rotate((x_max,y_max)),)

#Iterate over the exploration zone
scan_zone={}
zone={}
w=rotate((x_max,y_max))[0]
print(w)
for m in range(w+1):
    top=min(m,w-m)
    n=-top
    zone[m]=[]
    scan_zone[m]=[n,top]
    while n<=top:
        zone[m].append(n)
        n+=1
print(scan_zone)


def section_append(sections, new):
    """for section in sections:
        if """
    return sections

def addition(sec1, sec2):
    if sec1[0]>sec1[1] or sec2[0]>sec2[1]:
        raise Exception("Error on plans")
    elif sec1[1]+1<sec2[0] or sec1[0]>sec2[1]+1:
        return False
    else:
        sec=[]
        sec.append(min(sec1[0],sec2[0]))
        sec.append(max(sec1[1],sec2[1]))
        return sec

print("Addition : ", addition([10,12],[0,9]))

exit()

"""

#Check each line for hole ?
zone={}
w=rotate((x_max,y_max))[0]
print(w)
for m in range(w+1):
    top=min(m,w-m)
    start=-top
    end=top

    #Find all square including y=m
    plans_list=[]
    for p in plans:



    zone[m]=[]
    while n<=top:
        zone[m].append(n)
        n+=1



#Iterate on each point to find if inside a sensor/beacon circle
x_min=0
y_min=0
x_max=20
y_max=20
import time

ana_dict={}
start_time = time.time()

for x in range(x_min,x_max,1):
    time_now=time.time()
    print(x, time_now-start_time)
    for y in range(y_min,y_max,1):
        check=0
        for i in range(nb_sensors):
            if distance((x,y),sensors[i])<=distances[i]:
                break
            else:
                check+=1
        if check==nb_sensors: 
            print(x,y)

"""