import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np
import math
from numpy.random import *
import random

## matplot animaion
x1=[]
y1=[]
#y=np.arange(0,20,2)
data=rand(100)

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

#fig, ax = plt.subplots(2,1, figsize=(8,6))


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


##matplot pause
def pause_plot():
    fig, ax = plt.subplots(1, 1)
    X = np.arange(0,10000,1)
    Y = [random.randint(0, 10) for i in range(10000)]
    Y = [float(y) for y in Y]

    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.sin(x)

    print(len(x), len(y))
    # 初期化的に一度plotしなければならない
    # そのときplotしたオブジェクトを受け取る受け取る必要がある．
    # listが返ってくるので，注意
    lines, = ax.plot(X[:50],Y[:50])
    print(lines)

    # ここから無限にplotする
    for i in range(200):
        #x += 0.1
        #y = np.sin(x)


        #x = X[i]
        #y = Y[i]
        a=i*50
        x = X[a:a+50]
        y = Y[a:a+50]
        print(x, y)


        # plotデータの更新
        # 描画データを更新するときにplot関数を使うと
        # lineオブジェクトが都度増えてしまうので，注意．
        #
        # 一番楽なのは上記で受け取ったlinesに対して
        # set_data()メソッドで描画データを更新する方法．
        
        lines.set_data(x, y)

        # set_data()を使うと軸とかは自動設定されないっぽいので，
        # 今回の例だとあっという間にsinカーブが描画範囲からいなくなる．
        # そのためx軸の範囲は適宜修正してやる必要がある．
        
        ax.set_xlim((x.min(), x.max()))

        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(.1)

    
    

if __name__ == "__main__":
    Anime()
    #pause_plot()







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
