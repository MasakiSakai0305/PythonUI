import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
import math
from numpy.random import *

x1=[]
y1=[]
#y=np.arange(0,20,2)
data=rand(100)

x2=[9,8,7,6,5]
y2=[7,8,9,6,5]


def _update(frame, x, y, data):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # データを更新 (追加) する
    x.append(frame)
    y.append(data[frame])

    # 折れ線グラフを再描画する
    print(y)
    #print(len(y))
    plt.scatter(x, y)

#fig, ax = plt.subplots(2,1, figsize=(8,6))
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

#ax[1]=plt.plot(x2, y2)

fig.show()
plt.show()


"""
fig, ax = plt.subplots(2,1, figsize=(12,10))

x = sen_df2['times(s)']
for column in sen_df2.columns[1:]:
    y=sen_df2[column]
    ax[0].plot(x,y, label=column)
    ax[0].legend(loc='best',
           bbox_to_anchor=(1.05, 0.5, 0.2, .100),
           borderaxespad=0.,)
for column in sen_df2.columns[2:]:
    y=sen_df2[column]
    ax[1].plot(x,y, label=column)
    ax[1].legend(loc='best',
           bbox_to_anchor=(1.05, 0.5, 0.2, .100),
           borderaxespad=0.,)
"""
