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
#print(beacons)
#print(sensors)

def distance(s,b):
    d = abs(s[0]-b[0]) + abs(s[1]-b[1])
    return d

#Calculate distance for each beacon / sensor couple
distances=[]
for i in range(len(sensors)):
    distances.append(distance(sensors[i],beacons[i]))
print(distances)


#Iterate on each point to find if inside a sensor/beacon circle
x_min=0
y_min=0
x_max=20
y_max=20
nb_sensors=len(sensors)
ana_dict={}
for x in range(x_min,x_max,1):
    for y in range(y_min,y_max,1):
        check=0
        for i in range(nb_sensors):
            if distance((x,y),sensors[i])<=distances[i]:
                break
            else:
                check+=1
        if check==nb_sensors: 
            print(x,y)
