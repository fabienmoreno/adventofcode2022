f=open('06/input.txt','r').read()
check=[0,0,0,0,0,0]
for i in range(len(f)):
    check=[f[i]!=f[i+1],f[i]!=f[i+2],f[i]!=f[i+3],f[i+1]!=f[i+2],f[i+1]!=f[i+3],f[i+2]!=f[i+3]]
    if sum(check)==6:
        break
    else:
        check[4]=check[1]
        check[5]=check[3]
        check[3]=check[0]
        check[0]=0
        check[1]=0
        check[2]=0
        i+=1
print(i+4)