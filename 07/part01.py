f=open('07/input.txt','r')
l=f.read().split("\n")

dirs={"/":["dir1/","dir2/"],"/dir1/":["fol3/"]}
#Dictionnaire des dossier

files={"/":[132067,132067], "/dir1/":[125,2455], "/dir2/":[2455], "/dir1/fol3/":[512], }
#Dictionnaire des fichiers

status = ""
data=""
current_folder=""
for c in l:
    print(current_folder)
    if c[0:4]=="$ cd":
        location=c.replace("$ cd ","")
        if location=="..":
            current_folder=current_folder[0:current_folder.rindex("/")]
        else:
            current_folder=current_folder+"/"+location
    elif c[0:4]=="$ ls":
        pass
    elif c[0:2]=="dir":
        pass
    else:
        pass



#Calculate size of each folder
dir_sizes={}
"""
def sum_files(files, folder, parent=""):
    total=0
    total=sum(files[parent+folder])
    try:
        for f in dirs[parent+folder]:
            total+=sum_files(files,f,parent+folder)
    except KeyError:
        pass
    print(parent,folder,total)
    return total

print("total :",sum_files(files,"/"))"""

"""
counter={}
for line in l:
    try:
        counter[line]+=1
    except KeyError:
        counter[line]=1

counter={k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
print(counter)"""