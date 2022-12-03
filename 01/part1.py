f=open('01/input.txt','r')
c=0
s=0
for l in f:
    if l !='\n':
        s+=int(l)
    else:
        if s>c:
            c=s
        s=0
print (c)