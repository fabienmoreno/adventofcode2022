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

f=open('07/input.txt','r')
l=f.read().split("\n")
nav=Arbo("/")
for c in l:
    if c=='$ cd /': pass
    else :
        cl=c.split(" ")
        nav.com(cl)

dir_sizes={}

def folder_size(files, dirs, nav):
    global dir_sizes
    total = 0
    if nav.wd in files.keys():
        total=sum(files[nav.wd])
    if nav.wd in dirs.keys():
        for d in dirs[nav.wd]:
            sd=nav.wd+d+"/"
            total+=folder_size(files, dirs, Arbo(sd))
    dir_sizes[nav.wd]=total
    return total

nav=Arbo("/")
folder_size(files,dirs,nav)

capacity=70000000
space_required=30000000
space_used=dir_sizes["/"]
free_space=capacity-space_used
seuil=space_required-free_space
print("Space to be freed up : ", seuil)

size_delete=float('inf')
for d in dir_sizes:
    if dir_sizes[d]>seuil and dir_sizes[d]<size_delete:
        size_delete=dir_sizes[d]

print("Folder size to be deleted : ", size_delete)