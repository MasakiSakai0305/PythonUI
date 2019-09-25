import tkinter as tk
from PlotSensor import PlotSensor 

#Show ScrollBar
class ScrollBar():

    def __init__(self):
        pass

    #close window
    def _quit(self, root):
        root.quit()     
        root.destroy()

    #show plot when button is pushed
    def button_selected(self, lb):

        #anyone aren't selected
        if len(lb.curselection()) == 0:
            return
        
        index = lb.curselection()[0]
        label = lb.get(index)
        #path = 'resource/NG/12182700604BB524_NG.csv'
        
        plot = PlotSensor(label)
        plot.Plot()

    #get add data label
    def data_add(self, data):
        try:
            self.data = data
        except AttributeError:
            print('error')
            return
    

    #add getting new data label 
    def update(self, lb):
        lb.delete(0, 'end')
        try:
            for data in self.data:
                lb.insert('end', data)
        except AttributeError:
            print('error')
            return

    
    #Show scrollbar
    def Scroll(self, datalabel):
        self.datalabel = datalabel

        root = tk.Tk()
        root.title(u"ScrollBar")
        root.geometry("800x500")

        frame = tk.Frame(root, height=200, width=400, bg="white")
        frame.place(relwidth=0.9, relheight=0.9)
        frame.pack(padx=10, pady=10)

        # Listbox
        lb = tk.Listbox(frame, selectmode = 'single', height = 5, width = 40)
        lb.pack(side = 'left')

        # Scrollbar
        sb = tk.Scrollbar(frame, command = lb.yview)
        sb.pack(side = 'left', fill = 'y')
        lb.configure(yscrollcommand = sb.set)
        for x in sorted(datalabel):
            lb.insert('end', x)

        # button
        button_quit = tk.Button(root, text="Quit", command=lambda:self._quit(root))
        button_quit.pack()
        
        button_plot = tk.Button(root, text="Plot", command=lambda:self.button_selected(lb))
        button_plot.pack()

        button_update = tk.Button(root, text="update", command=lambda:self.update(lb))
        button_update.pack()
        tk.mainloop()