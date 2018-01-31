import os
import fnmatch

MTS = []
MTS = fnmatch.filter(os.listdir('.'), '*.MTS')
MTS.sort()
for i in MTS:
    print("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mp4")
    os.system("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mp4")
    

#MP4 = []
#MP4 = fnmatch.filter(os.listdir('.'), '*.mp4')
#MP4.sort()
#for i in MP4:
#    print("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")
#    os.system("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")
os.system("mencoder -oac pcm -ovc copy -o merged_file.mp4 `ls *.mp4`")    
os.system("avconv -i merged_file.mp4 -c copy film.mkv")
#kvmerge -o full.mkv file1.mkv + file2.mkv
#$ mkvmerge -o full.mkv '[' file1.mkv file2.mkv ']'
# source https://mkvtoolnix.download/doc/mkvmerge.html

#MKV = []
#MKV = fnmatch.filter(os.listdir('.'), '*.mkv')
#MKV.sort()
#s_mkv = ''
#count=1
#for j in MKV:
#    if count==1:
#        os.system("mkvmerge -o ../full.mkv "+j)
#        os.system("mv ../full.mkv ../last.mkv")
#        
#    else:
#        os.system("mkvmerge -o ../full.mkv ../last.mkv "+j)
#        os.system("rm ../last.mkv")
#        os.system("mv ../full.mkv ../last.mkv")
#    count=count+1
#    print(count)        
    
    #s_mkv = s_mkv+" "+j
print('###############################################')
os.system('rm *mp4')
# print("mkvmerge -o ../full.mkv "+s_mkv)
# os.system("mkvmerge -o ../full.mkv "+s_mkv)
# os.system("rm *.mkv")