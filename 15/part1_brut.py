f=open('15/input.txt','r').read()
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
print(beacons)
print(sensors)


def layers(r):
    points = []
    if r==0: raise Exception("Layer zero")
    for k in range(-r,r,1):
        px=k
        py=r-abs(k)
        points.append((px,py))
        points.append((-px,-py))
    return points

def distance(s,b):
    d = abs(s[0]-b[0]) + abs(s[1]-b[1])
    return d

def fill_beacon(sensor,beacon):
    no_beacon=[]

    #Calculate distance
    d=distance(sensor,beacon)
    if d==0: raise Exception("Sensor over Beacon")
    print(d)

    #Fill every layer
    for j in range(1, d+1):
        ll=layers(j) #Return a list of points forming the layer
        for p in ll:
            no_beacon.append(p)
    
    return no_beacon #Return a list of tupple of point which cannot contain another beacon

#3,0 2,1 1,2 0,3 -1,2 -2,1 -3,0 
#

#Definie a set of not accessible points
row=2000000

no_beacon = set()
for i in range(len(sensors)):
    locations = fill_beacon(sensors[i],beacons[i])
    for l in locations:
        no_beacon.add((l[0]+sensors[i][0],l[1]+sensors[i][1]))
    #print(i, no_beacon)
#print(no_beacon)

#Check number of occupied location on a specific row

counter=0
for p in no_beacon:
    if p[0]==row: counter+=1
print ("Number of occupied locations : ", counter)
