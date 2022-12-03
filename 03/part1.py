f=open('03/input.txt','r')
l=f.read().split("\n")
import string
s=0
for m in l:
    le=int(len(m)/2)
    a=m[0:le]
    b=m[le:]
    for j in a:
        if j in b:
            s+=string.ascii_letters.index(j)+1
            break
print(s)