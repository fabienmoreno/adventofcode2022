f=open('10/input.txt','r')
l=f.read().split("\n")

cycles=[1]

for c in l:
    if c=="noop": 
        cycles.append(0)
    elif c[0:4]=="addx":
        com=c.split(" ")
        incr=int(com[1])
        cycles.append(0)
        cycles.append(incr)

cumul=[(0,1)]
crt=[]
for i,v in enumerate(cycles):
    if i>0: cumul.append((i, v+cumul[i-1][1]))
for i in cumul:
    if abs(i[0]%40-i[1])<=1: crt.append("#")
    else: crt.append(".")

for i in range(6):
    col=40
    print(crt[i*col:(i+1)*col])

