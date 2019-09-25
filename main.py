import os
import glob
import threading

#Module import
from ui_menu import UI_MEnu as UI
from scroll import ScrollBar

labels=[]
os.chdir('resource/NG/')

for i in glob.glob("./*"):
    label = i.split('/')[1]
    labels.append(label)


ui = UI(labels)

def dataAdd():
    global labels
    while True:
        addlabels=[]
        #time.sleep(3)
        for i in glob.glob("./*"):
            label = i.split('/')[1]
            addlabels.append(label)
        ui.labels = addlabels
        #print(labels)
        ui.sc.data_add(addlabels)

def hoge():
    print('hoge')

thread1 = threading.Thread(target=ui.Button)
thread2 = threading.Thread(target=dataAdd)
thread3 = threading.Thread(target=hoge)
thread1.start()
thread2.start()
thread3.start()


