f=open('03/input.txt','r')
l=f.read().split("\n")
p=int(len(l))
import string
s=0
for i in range(0,p,3):
    a=l[i]
    b=l[i+1]
    c=l[i+2]
    for j in a:
        B=b.count(j)
        C=c.count(j)
        if B>=1 and C>=1:
            s+=string.ascii_letters.index(j)+1
            break
print(s)