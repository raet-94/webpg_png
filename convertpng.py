from os import listdir
from os.path import isfile, join
from PIL import Image

sufix = "webp"
new_sufix="png"
folder_up= "/home/rodrigo/data1/stickers/"
old_folder ="webpg"
new_folder ="png"
#print(folder_up + old_folder)
onlyfiles = [f for f in listdir(folder_up + old_folder) if isfile(join(folder_up + old_folder, f))]
onlyfiles_sufix = [file for file in onlyfiles if sufix in str(file)]

for i in range(len(onlyfiles_sufix)):
    name =onlyfiles_sufix[i]
    new_name = name.replace(sufix, new_sufix)
    im = Image.open(folder_up+old_folder+"/"+name).convert("RGB")
    im.save(folder_up+new_folder+"/"+new_name,new_sufix)
    