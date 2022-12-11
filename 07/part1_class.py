class Nav:
    def __init__(self,wd):
        self.wd=wd
    def wd(self):
        return self.wd()
    def cd(self,cd):
        if "/" in cd: raise Exception("/ caracter not allowad in cd ")
        if self.wd=="/": 
            raise Exception("WD already in top directory")
            pass
        if cd=="..":
            self.wd=self.wd[0:-1]
            self.wd=self.wd[0:self.wd.rindex("/")+1]
        else: self.wd=self.wd+cd+"/"
    def getParent(self):
        self.wd=self.wd[0:-1]
        self.wd=self.wd[0:self.wd.rindex("/")+1]
        return self.wd
    def goDir(self,d):
        self.wd=self.wd+d+"/"
        return self.wd

"""nav=Nav("/")
a=nav.wd
print(a)
nav.cd("hello")
nav.cd("test")
print(nav.wd)
nav.cd('..')
print(nav.wd)
nav.cd('..')
print(nav.wd)"""
dirs={}
files={}

class Arbo:
    #Command interpreter
    def __init__(self,wd):
        self.wd=wd
    def wd(self):
        return self.wd()
    def com(self,arg):
        global dirs
        global files
        if arg[0]=="$":
            if arg[1]=="cd":
                if arg[2]=="..":
                    if self.wd=="/": 
                        raise Exception("WD already in top directory")
                        pass
                    else:
                        self.wd=self.wd[0:-1]
                        self.wd=self.wd[0:self.wd.rindex("/")+1]
                elif c!="..":
                    if "/" in arg[2]: raise Exception("/ caracter not allowed in cd ")
                    else: self.wd=self.wd+arg[2]+"/"
        elif arg[0]=="dir": #If return directory description
            if self.wd in dirs.keys():
                dirs[self.wd].append(arg[1])
            else:
                dirs[self.wd]=[arg[1]]
        elif arg[0].isdigit(): #If return file description
            if self.wd in files.keys(): files[self.wd].append(int(arg[0]))
            else: files[self.wd]=[int(arg[0])]


f=open('07/simple.txt','r')
l=f.read().split("\n")
nav=Arbo("/")
for c in l:
    if c=='$ cd /': pass
    else :
        cl=c.split(" ")
        nav.com(cl)

print(dirs)
print(files)

dir_sizes={}
nav=Nav("/")

def folder_size(files, dirs, nav):
    total=sum(files[nav.wd])
    print(nav.wd)
    if nav.wd in dirs.keys():
        for d in dirs[nav.wd]:
            nav.goDir(d)
            total+=folder_size(files, dirs, nav)
    return total

print(folder_size(files,dirs,nav))

#a=nav.getParent()




print(dir_sizes)



"""
c="$ cd a".split(" ")
nav.com(c)
print(nav.wd)

c="$ cd b".split(" ")
nav.com(c)
print(nav.wd)

c="dir f".split(" ")
nav.com(c)
print(nav.wd)
print(dirs)

c="8504156 c.dat".split(" ")
nav.com(c)
print(nav.wd)
print(dirs)

c="$ ls".split(" ")
nav.com(c)
print(nav.wd)

c="$ cd ..".split(" ")
nav.com(c)
print(nav.wd)

c="dir e".split(" ")
nav.com(c)
print(nav.wd)
print(dirs)
print(files)

"""