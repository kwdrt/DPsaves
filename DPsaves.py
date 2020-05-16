#DPsavesaver
from datetime import datetime
from shutil import copy
from os import rename,path
import hashlib
from glob import glob
from time import sleep

# Put your savefile location in src, put another \ before every ' or \ character (ex. Director 's Cut -> Director \'s Cut)
# Put your backup folder location in dst, make one beforehand
# Example paths are already entered, yours are probably similar


while(1):
    src = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Deadly Premonition The Director\'s Cut\\savedata\\dp.sav"
    dst = "C:\\bckup\\dp\\"

    now=datetime.now()
    time=now.strftime("%Y%b%d--%H-%M-%S")

    list_of_files=glob(dst + '\\*')
    if(list_of_files)!=[]:
        latest = max(list_of_files, key=path.getctime)

        hash1 = hashlib.md5()
        newsav = open(src, 'rb')
        buf1 = newsav.read()
        newsav.close()
        a = hash1.update(buf1)
        md5_a=(str(hash1.hexdigest()))

        hash2 = hashlib.md5()
        lastsav = open(latest, 'rb')
        buf2 = lastsav.read()
        lastsav.close()
        b = hash2.update(buf2)
        md5_b=(str(hash2.hexdigest()))

        if(md5_a!=md5_b):
            print("New save found, making copy")
            copy(src, dst)
            put = dst + 'dp.sav'
            new = dst + 'dp-{}.sav'.format(time)
            rename(put,new)
    else:
        print("First save found, making copy")
        copy(src, dst)
        put = dst + 'dp.sav'
        new = dst + 'dp-{}.sav'.format(time)
        rename(put,new)
        
    print("No new save found")
    sleep(300)
