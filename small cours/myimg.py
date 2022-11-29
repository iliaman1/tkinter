import tkinter as tk


class MyIMG(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('contact list')
        self.geometry('320x240')
        self.iconphoto(False, tk.PhotoImage(file='img/photo.png'))

        self.canva = tk.Canvas()
        self.canva.pack()

        self.canva.create_oval(140, 20, 180, 60, fill='orange', outline='yellow')
        self.canva.create_polygon(60, 100, 100, 60, 140, 100, fill='lightblue')
        self.canva.create_rectangle(80, 100, 120, 140, fill='lightblue', outline='lightblue')
        self.canva.create_arc(40, 160, 60, 140, start=160, extent=-70,
                              style=tk.ARC, outline='darkgreen',
                              width=5)
        self.canva.create_arc(60, 160, 80, 140, start=160, extent=-70,
                              style=tk.ARC, outline='darkgreen',
                              width=5)
        self.canva.create_arc(80, 160, 100, 140, start=160, extent=-70,
                              style=tk.ARC, outline='darkgreen',
                              width=5)
        self.canva.create_arc(100, 160, 120, 140, start=160, extent=-70,
                              style=tk.ARC, outline='darkgreen',
                              width=5)
        self.canva.create_arc(120, 160, 140, 140, start=160, extent=-70,
                              style=tk.ARC, outline='darkgreen',
                              width=5)


if __name__ == '__main__':
    root = MyIMG()
    root.mainloop()
