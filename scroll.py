import tkinter as tk
from PlotSensor import PlotSensor 



#Show ScrollBar Display
class ScrollBar():

    def __init__(self):
        pass

    #close window
    def _quit(self, root):
        root.quit()     
        root.destroy()

    def button_selected(self, lb):
        if len(lb.curselection()) == 0:
            return
        index = lb.curselection()[0]
        print(lb.get(index))
        path = 'resource/NG/12182700604BB524_NG.csv'
        plot = PlotSensor(path)
        plot.Plot()

    def data_add(self, added_data):
        self.added_data = added_data


    def update(self, lb):
        if self.added_data == 0:
            return
        lb.insert('end', self.added_data)
        self.added_data = 0

    
    #Show scrollbar
    def Scroll(self, datalabel):
        root = tk.Tk()
        root.title(u"Show Sensor Datas")
        root.geometry("800x500")

        frame = tk.Frame(root, height=200, width=400, bg="white")
        frame.place(relwidth=0.9, relheight=0.9)

        frame.pack(padx=10, pady=10)
        # リストボックスの生成
        lb = tk.Listbox(frame, selectmode = 'single', height = 10, width = 40)
        lb.pack(side = 'left')

        # スクロールバーの生成
        sb = tk.Scrollbar(frame, command = lb.yview)
        sb.pack(side = 'left', fill = 'y')

        lb.configure(yscrollcommand = sb.set)

        # バインディング
        #lb.bind('<<ListboxSelect>>', ani)

        for x in sorted(datalabel):
            lb.insert('end', x)

        button_quit = tk.Button(root, text="Quit", command=lambda:self._quit(root))
        button_quit.pack()
        
        button_plot = tk.Button(root, text="Plot", command=lambda:self.button_selected(lb))
        button_plot.pack()

        button_update = tk.Button(root, text="update", command=lambda:self.update(lb))
        button_update.pack()
        tk.mainloop()