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
print(beacons)
print(sensors)


def layers(r,row):
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

def fill_beacon(sensor,beacon,row):
    no_beacon=[]

    if row>sensor[1]+abs(sensor[1]-beacon[1])*2 or row<sensor[1]-abs(sensor[1]-beacon[1])*2:
        return no_beacon
    else:
        #Calculate distance
        d=distance(sensor,beacon)
        if d==0: raise Exception("Sensor over Beacon")
        print(d)

        for x in range(sensor[0]-2*d,sensor[0]+2*d,1):
            if distance(sensor, (x,row))<=d:
                no_beacon.append(x)
        return no_beacon #Return a list of tupple of point which cannot contain another beacon

#3,0 2,1 1,2 0,3 -1,2 -2,1 -3,0 
#

#Definie a set of not accessible points

no_beacon = set()
nob_list=[]
row=10

for i in range(len(sensors)):
    locations = fill_beacon(sensors[i],beacons[i],row)
    nob_list+=locations
    #print(i, no_beacon)
#print(no_beacon)

indepedent_locations = set(nob_list)
print(indepedent_locations)
print ("Number of occupied locations : ", len(indepedent_locations))
