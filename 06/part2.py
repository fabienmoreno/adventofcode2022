f=open('06/input.txt','r').read()
l=14 #marker length
m={} #Init count dictionary
def add_dict(dict, key):
    try: dict[key]+=1
    except KeyError: dict[key]=1
for i in range(l): add_dict(m, f[i])
for i in range(len(f)):
    if max(m.values())>1:
        m[f[i]]=m[f[i]]-1
        add_dict(m, f[i+l])
    else: break
print(i+l)