import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib.animation as an

class Animation():
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data

    #close window
    def _quit(self, root):
        root.quit()     
        root.destroy()

    def _update(self, frame, x, y, data):
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


    def ani(self):
        root = tk.Tk()
        fig = plt.figure(figsize=(10, 6))
        params = {
            'fig': fig,
            'func': self._update,  # グラフを更新する関数
            'fargs': (self.x, self.y, self.data),  # 関数の引数 (フレーム番号を除く)
            'interval': 10,  # 更新間隔 (ミリ秒)
            'frames': np.arange(0, 100, 1),  # フレーム番号を生成するイテレータ
            'repeat': False,  # 繰り返さない
        }
        canvas = FigureCanvasTkAgg(fig, master=root)
        anime = an.FuncAnimation(**params)


        toolbar = NavigationToolbar2Tk(canvas, root)
        canvas.get_tk_widget().pack()

        button = tk.Button(master=root, text="Quit", command=lambda:self._quit(root))
        button.pack()
        tk.mainloop()