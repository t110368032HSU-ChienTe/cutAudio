
import shutil
import os
import csv



data_folder="voice1_cutVad_fullsubnet"
save_folder="voice1_cutVad_fullsubnet_180"

refer_csv="result_fullsubnet_180.csv"

speakers = os.listdir(data_folder)

with open(refer_csv, newline='') as csvfile:
    rows = csv.reader(csvfile)    

    for row in rows:
        for speaker in row:
            if speaker in speakers:
                referPath = os.path.join(data_folder,speaker)
                newPath   = os.path.join(save_folder,speaker)
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
                shutil.copyfile(referPath,newPath)
                print("第{}位，名稱:{}".format(int(row.index(speaker))+1,speaker))
                

