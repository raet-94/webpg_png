import multiprocessing
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
onlyfiles_newsufix = [file.replace(sufix, new_sufix) for file in onlyfiles_sufix]
complete_old_names =[folder_up+old_folder+"/"+file for file in onlyfiles_sufix ]
complete_new_names =[folder_up+new_folder+"/"+file for file in onlyfiles_newsufix]
new_tuples =[[complete_old_names[i],complete_new_names[i]] for i in range(len(complete_old_names))] 

def convertwebp_topng(tuppleofnames):
    old_name= tuppleofnames[0]
    new_name = tuppleofnames[1]
    im = Image.open(old_name).convert("RGB")
    im.save(new_name,"png")


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    result_list = pool.map(convertwebp_topng, new_tuples)
    pool.close()
