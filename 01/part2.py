f=open('01/input.txt','r')
cl=[0,0,0]
s=0
def push(L,s):
    for i in range(len(L)):
        if s>L[i]:
            if i!=0: L[i-1]=L[i]
            L[i]=s   
    return L
for l in f:
    if l !='\n':
        s+=int(l)
    else:
        push(cl,s)
        s=0
print (cl)
print(sum(cl))