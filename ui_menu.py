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


class UI_MEnu():

    def __init__(self, labels):
        self.sc = ScrollBar()
        self.labels = labels

    #close window
    def _quit(self, root):
        root.quit()     
        root.destroy()
        os._exit(1)

    def Menu(self):
        pass

    def Button(self):
        self.root=tk.Tk()
        self.root.title(u"EAP View Data")
        self.root.geometry("800x500")

        x1=[]
        y1=[]
        data=rand(100)
        
        #Show Animation
        an = Animation(x1, y1, data)
        Button1 = tk.Button(text=u'plot result', master=self.root, command=an.ani)
        Button1.pack()

        #Plot Sensordata
        path = 'resource/NG/12182700604BB524_NG.csv'
        plot = PlotSensor(path)
        button_plot_sen = tk.Button(text=u'Plot Sensor', master=self.root, command=plot.Plot)
        button_plot_sen.pack()

        #Show ScrollBar
        #data=[1,2,3]
        #sc = ScrollBar()
        button_data = tk.Button(text=u'ScrollBar', master=self.root, command=lambda:self.sc.Scroll(self.labels))
        print(self.sc)
        button_data.pack()

        #Quit
        button_quit = tk.Button(master=self.root, text="Quit", command=lambda:self._quit(self.root))
        button_quit.pack()

        self.root.mainloop()