'''
This script is my poc how to merge MTS files
from my video camera to one large video
and convert to mkv
'''

from __future__ import print_function

import os
import fnmatch

MTS = []
MTS = fnmatch.filter(os.listdir('.'), '*.MTS')
MTS.sort()
for i in MTS:
    print("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mp4")
    os.system("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mp4")


MP4 = []
MP4 = fnmatch.filter(os.listdir('.'), '*.mp4')
MP4.sort()
for i in MP4:
    print("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")
    os.system("ffmpeg -i "+i+" -vcodec copy -acodec copy "+i[:-4]+".mkv")

os.system('rm *mp4')

MKV = []
MKV = fnmatch.filter(os.listdir('.'), '*.mkv')
MKV.sort()
count = 0
for i in MKV:
    if (count == 0):
        os.system("mkvmerge -o full0.mkv "+ i)
    if (count > 0):
        print("#################################################################")
        print("mkvmerge -o full"+str(count)+".mkv full" +str(count-1)+".mkv + "+i)
        os.system("mkvmerge -o full"+str(count)+".mkv full" +str(count-1)+".mkv + "+i)
        if os.path.exists("full" +str(count-1)+".mkv"):
            os.remove("full" +str(count-1)+".mkv")
        if os.path.exists(i):
            os.remove(i)
            
    count = count+ 1
    print('count: '+str(count))
os.rename("full" +str(count-1)+".mkv", "complete.mkv")
