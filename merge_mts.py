import os
import fnmatch

MTS = []
MTS = fnmatch.filter(os.listdir('.'), '*.MTS')
MTS.sort()
for i in MTS:
    print("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")
    # os.system("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")
    
#kvmerge -o full.mkv file1.mkv + file2.mkv
#$ mkvmerge -o full.mkv '[' file1.mkv file2.mkv ']'
# source https://mkvtoolnix.download/doc/mkvmerge.html

MKV = []
MKV = fnmatch.filter(os.listdir('.'), '*.mkv')
MKV.sort()
s_mkv = ''
count=1
for j in MKV:
    if count==1:
        os.system("mkvmerge -o ../full.mkv "+j)
        os.system("mv ../full.mkv ../last.mkv")
        
    else:
        os.system("mkvmerge -o ../full.mkv ../last.mkv "+j)
        os.system("rm ../last.mkv")
        os.system("mv ../full.mkv ../last.mkv")
    count=count+1
    print(count)        
    
    #s_mkv = s_mkv+" "+j
print('###############################################')

# print("mkvmerge -o ../full.mkv "+s_mkv)
# os.system("mkvmerge -o ../full.mkv "+s_mkv)
# os.system("rm *.mkv")