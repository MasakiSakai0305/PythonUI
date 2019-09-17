import tkinter
import sys

root=tkinter.Tk()
root.title(u"Button")
root.geometry("400x300")

Button1 = tkinter.Button(text=u'Button1')
Button2 = tkinter.Button(text=u'Button2')
Button1.pack()
Button2.pack()

root.mainloop()