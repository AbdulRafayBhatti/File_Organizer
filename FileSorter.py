import os, shutil
path = input("Enter the folder path you  want to sort: ")
path+='\\'
files = os.listdir(path)
folders = set()
try:
    for file in files:
        if(os.path.isfile(path+file)):
            indx = file.rfind('.')
            if(indx != -1):
                fnym = file[indx+1:]
                if(fnym.upper() in folders):
                    shutil.move(path + file, path+fnym.upper() + '\\' + file)
                else:
                    folders.add(fnym.upper())
                    os.makedirs(path+fnym.upper())
                    shutil.move(path + file, path+fnym.upper() + '\\' + file)
            else:
                print(file+" has no extension.")
    print("Sorted Successfully.")
except Exception as e:
    print("Error Occurs: \n" + str(e))

    