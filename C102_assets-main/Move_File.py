import os
import shutil
from_dir = "Downloads"
to_dir = "Destination"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name, extention = os.path.splitext(file)
    print(name)
    print(extention)
    if(extention == ""):
        continue
    if(extention in ['.txt','.doc','.docx','.pdf']):
        path1 = from_dir+'/'+file
        path2 = to_dir+'/'+"Document_Files"
        path3 = to_dir +'/'+"Document_Files"+'/'+file
        if(os.path.exists(path2)):
            print("Moving "+file+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving"+file+"...")
            shutil.move(path1,path3)
