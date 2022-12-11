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

i=[20,60,100,140,180,220]
c=0
for i in i:
    c+=sum(cycles[0:i])*i
print(c)
