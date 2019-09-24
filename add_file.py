#write file pythonfile
#update data label

import time
import glob

path = 'resource/NG/DammyData'

def addfile(path):
    s = 'This is dammy data'
    with open(path, mode='w') as f:
        f.write(s)
    print('complete write file:', path)

if __name__ == '__main__':
    for i in range(1,11):
        addfile(path + '{}.txt'.format(i))
        time.sleep(5)
   
    