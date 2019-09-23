import tkinter as tk
import sys
from numpy.random import *
import time

#Module import
from PlotSensor import PlotSensor 
from scroll import ScrollBar
from PlotAnimation import Animation

x1=[]
y1=[]
data=rand(100)


#close window
def _quit(root):
    root.quit()     
    root.destroy()


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
data=[1,2,3]
sc = ScrollBar()
button_data = tk.Button(text=u'ScrollBar', master=root, command=lambda:sc.Scroll(data))
button_data.pack()
time.sleep(5)
sc.data_add(4)



#Quit
button_quit = tk.Button(master=root, text="Quit", command=lambda:_quit(root))
button_quit.pack()
root.mainloop()


