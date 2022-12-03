f=open('01/input.txt','r')
a = [sum(int(i) for i in x.split()) for x in f.read().split("\n\n")]
print(a)