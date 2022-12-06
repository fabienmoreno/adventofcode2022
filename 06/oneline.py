str=open('06/input.txt','r').read()
l=14
print(next(i for i,v in enumerate([len(str[i:i+l])==len(set("".join(str[i:i+l]))) for i in range(len(str)-l)]) if v)+l)