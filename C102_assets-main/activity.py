import os
import shutil

source = "images"
destination = "organized_files"

listOfFiles = os.listdir(source)

for file in listOfFiles:
    filename, fileExtention = os.path.splitext(file)
    if(fileExtention == ""):
        continue
    if(fileExtention in [".jpg", ".png",".gif",".jfif"]):
        path1 = source + "/"+file #the files inside the source folder
        path2 = destination+"/"+"image_files"
        path3 = destination+"/"+"image_files"+"/"+file
        if(os.path.exists(path2)):
            print("image folder exists")
            shutil.move(path1,path3)
            print("files are moved")
        else:
            print("folder doesn't exist")
            print("Creating image folder")
            os.mkdir(path2)
            print("moving files")
            shutil.move(path1,path3)
            print("file is moved")            
        

# print(dir(os))
#print(os.getcwd())

# os.rename("example.txt","example_1.txt")

# path = "example_1.txt"

# if(os.path.exists(path)):
#   print("path exits")
# else:
#   print("doesn't exist")

# os.mkdir("test")
# os.remove("example_1.txt")

#file = "example.txt"

#file_name , extension = os.path.splitext(file)
#print(file_name)
# print(extension)