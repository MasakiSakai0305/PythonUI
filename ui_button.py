import tkinter as tk
import sys
from numpy.random import *
import time
import glob
import os
import threading


#Module import
from PlotSensor import PlotSensor 
from scroll import ScrollBar
from PlotAnimation import Animation


sc = ScrollBar()
labels=[]
#os.chdir('resource/dammy/')
os.chdir('resource/NG/')

for i in glob.glob("./*"):
    label = i.split('/')[1]
    labels.append(label)


#close window
def _quit(root):
    root.quit()     
    root.destroy()
    os._exit(1)

def menu():
    x1=[]
    y1=[]
    data=rand(100)

    root=tk.Tk()
    root.title(u"EAP View Data")
    root.geometry("800x500")


    #Show Animation
    an = Animation(x1, y1, data)
    Button1 = tk.Button(text=u'plot result', master=root, command=an.ani)
    Button1.pack()

    #Plot Sensordata
    path = 'resource/NG/12182700604BB524_NG.csv'
    plot = PlotSensor(path)
    button_plot_sen = tk.Button(text=u'Plot Sensor', master=root, command=plot.Plot)
    button_plot_sen.pack()

    #Show ScrollBar
    #data=[1,2,3]
    button_data = tk.Button(text=u'ScrollBar', master=root, command=lambda:sc.Scroll(labels))
    button_data.pack()

    #Quit
    button_quit = tk.Button(master=root, text="Quit", command=lambda:_quit(root))
    button_quit.pack()
    root.mainloop()

def hoge():
    time.sleep(5)
    print('5 second passed')

#always check folder 
#when new label appear, add it
def dataAdd():
    while True:
        global labels
        addlabels=[]
        time.sleep(3)

        for i in glob.glob("./*"):
            label = i.split('/')[1]
            addlabels.append(label)
        labels = addlabels
        sc.data_add(addlabels)

        """
        print(glob.glob("./*"))
        for i in glob.glob("./*"):
            label = i.split('/')[1]
            if label in labels:
                pass
            

            else:
                new_label = label
                labels.append(new_label)
                print(new_label)
                sc.data_add(new_label)
        """
    
thread1 = threading.Thread(target=menu)
thread2 = threading.Thread(target=hoge)
thread3 = threading.Thread(target=dataAdd)

thread1.start()
thread2.start()
thread3.start()
#thread1.join()
#thread2.join()


