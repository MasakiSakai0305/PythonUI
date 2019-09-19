import tkinter
import sys
import ui_gragh as gragh
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from numpy.random import *
import matplotlib.animation as an
import numpy as np


x1=[]
y1=[]
data=rand(100)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def _update(frame, x, y, data):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # データを更新 (追加) する
    x.append(frame)
    y.append(data[frame])

    # 折れ線グラフを再描画する
    #print(y)
    #print(len(y))
    plt.scatter(x, y)

def Anime():
    fig = plt.figure(figsize=(10, 6))
    params = {
        'fig': fig,
        'func': _update,  # グラフを更新する関数
        'fargs': (x1, y1, data),  # 関数の引数 (フレーム番号を除く)
        'interval': 10,  # 更新間隔 (ミリ秒)
        'frames': np.arange(0, 100, 1),  # フレーム番号を生成するイテレータ
        'repeat': False,  # 繰り返さない
    }
    anime = an.FuncAnimation(**params)
    fig.show()
    plt.show()


root=tkinter.Tk()
root.title(u"Button")
root.geometry("400x300")

#canvas = FigureCanvasTkAgg(fig, master=root)
#toolbar = NavigationToolbar2Tk(canvas, root)
#canvas.get_tk_widget().pack()

Button1 = tkinter.Button(text=u'show plot', master=root, command=Anime)
Button1.pack()

Button2 = tkinter.Button(text=u'Button2', master=root)
Button2.pack()

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack()

root.mainloop()