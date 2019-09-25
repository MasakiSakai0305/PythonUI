import tkinter
import sys
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
import pandas as pd


class PlotSensor():
    def __init__(self, path):
        self.path = path

    #close window
    def _quit(self, root):
        root.quit()     
        root.destroy()  
    
    #Plot SEnsor Data
    def Plot(self):
        root = tkinter.Tk()
        #path='resource/NG/12182700604BB524_NG.csv'
        title = self.path.split('.')[0]
        root.title(title)
        
        sen = pd.read_csv(self.path, index_col=0, encoding="shift-jis")
        sen = sen.rename(columns={'ﾁｯﾌﾟｽﾄﾛｰｸ量': 'Tip stroke', '射出速度': 'Injection speed',
                                    '鋳造圧力': 'Casting pressure', '真空度': 'Vacuum'})

        fig, ax = plt.subplots(2,1, figsize=(10,6))
        x = sen['時間']
        for column in sen.columns[1:]:
            y=sen[column]
            ax[0].plot(x,y, label=column)
            ax[0].legend(loc='best',
                bbox_to_anchor=(0.95, 0.8, 0.2, .100), 
                borderaxespad=0.,)
        for column in sen.columns[2:]:
            y=sen[column]
            ax[1].plot(x,y, label=column)
            ax[1].legend(loc='best',
                bbox_to_anchor=(0.95, 0.8, 0.2, .100), 
                borderaxespad=0.,)

        canvas = FigureCanvasTkAgg(fig, master=root)
        toolbar = NavigationToolbar2Tk(canvas, root)
        canvas.get_tk_widget().pack()

        button = tkinter.Button(master=root, text="Quit", command=lambda:self._quit(root))
        button.pack()
        tkinter.mainloop()