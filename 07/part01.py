f=open('07/simple.txt','r')
l=f.read().split("\n")


#Dictionnaire des dossier
#dirs={"/":["dir1/","dir2/"],"/dir1/":["fol3/"]}
#Dictionnaire des fichiers
#files={"/":[132067,132067], "/dir1/":[125,2455], "/dir2/":[2455], "/dir1/fol3/":[512], }

dirs={}
files={}
current_folder=""
for c in l:
    if c[0:4]=="$ cd":
        location=c.replace("$ cd ","")
        if location=="..": current_folder=current_folder[0:current_folder.rindex("/",0,len(current_folder)-1)]+"/"
        elif location=="/": current_folder="/"
        else: current_folder=current_folder+location+"/"
        #print(current_folder)
    elif c[0:4]=="$ ls":
        pass
    elif c[0:3]=="dir":
        dname=c[c.index(" ")+1:]
        if current_folder in dirs.keys(): 
            dirs[current_folder].append(dname)
        else: dirs[current_folder]=[dname]
    else:
        fsize=int(c[0:c.index(" ")])
        if current_folder in files.keys(): 
            files[current_folder].append(fsize)
        else: files[current_folder]=[fsize]


#Calculate size of each folder
dir_sizes={}

def sum_files(files, dirs, folder, parent=""):
    #total=0
    total=sum(files[parent+folder])
    try:
        for f in dirs[parent+folder]:
            total+=sum_files(files,dirs,f,parent+folder)
    except KeyError:
        pass
    print(parent,folder,total)
    return total

print(dirs)
print(files)

def sum_file_sizes(files, dirs, folder='/'):
    print(folder)
    total=sum(files[folder])
    for i in dirs[folder]:
        total+=sum_file_sizes(files, dirs, "/"+i+"/")
    return total

print("total :",sum_file_sizes(files, dirs, "/"))

"""counter={}
for line in l:
    try:
        counter[line]+=1
    except KeyError:
        counter[line]=1

counter={k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
print(counter)"""