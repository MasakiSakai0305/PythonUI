#色々試す用
import tkinter as tk
root = tk.Tk()


def hello():
    print("Hello")

def _quit():
    root.quit()     
    root.destroy()

var = tk.StringVar()
var.set("Hello")
def update_label():
    import random
    label_list = ["HOGE", "YES", "NO"]
    var.set(random.choice(label_list))

label = tk.Label(root, textvariable=var)
label.pack()
button = tk.Button(root, text="update", command=update_label)
button.pack()

b=tk.Button(root, text="quit", command=_quit)
b.pack()

root.mainloop()


"""
import tkinter as tk

import tkinter.font as font

root = tk.Tk()

# フォントの選択
def get_font(event):
    xs = lb.curselection()
    if len(xs) != 0:
        la.configure(font = (lb.get(xs[0]), 12))

# ラベルの生成
la = tk.Label(root, text = "Hello, world!, こんにちは世界!!", font = ('', 12))
la.pack(fill = tk.X)

# リストボックスの生成
lb = tk.Listbox(root, selectmode = 'single', height = 20, width = 40)
lb.pack(side = 'left')

# スクロールバーの生成
sb = tk.Scrollbar(root, command = lb.yview)
sb.pack(side = 'left', fill = 'y')

lb.configure(yscrollcommand = sb.set)

# バインディング
lb.bind('<<ListboxSelect>>', get_font)
a=list(range(0,100))
for x in sorted(a):
    lb.insert('end', x)

root.mainloop()
"""
