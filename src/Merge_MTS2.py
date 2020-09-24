import os
import subprocess

sdcard = "sdcard27"
directory = "Videos/"+sdcard+"/PRIVATE/AVCHD/BDMV/STREAM/"
file_names =[]
for file in os.listdir(directory):
    if file.endswith(".MTS"):
        file_names.insert(0,file)
file_names.sort()        
print(file_names)

text_file=open('file_list.txt','w')

for i in file_names:
    print("file \'"+directory+i+"\'\n")
    text_file.write("file \'"+directory+i+"\'\n")
    
text_file.close
bashCommand = "ffmpeg -f concat -i file_list.txt -c copy "+sdcard+".mkv"
print("run from command line:")
print(bashCommand)
#os.system(bashCommand)