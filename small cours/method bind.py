import tkinter as tk


class Events(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('event + listbox')
        self.geometry('140x200')
        self.iconphoto(False, tk.PhotoImage(file='img/event.png'))

        self.top_frame = tk.Frame()
        self.bot_frame = tk.Frame()
        self.ent = tk.Entry(self.top_frame)
        self.market_box = tk.Listbox(self.bot_frame, selectmode=tk.EXTENDED)
        self.scroll_market = tk.Scrollbar(self.bot_frame, command=self.market_box.yview)

        self.top_frame.pack(fill='x')
        self.bot_frame.pack(fill='both')
        self.ent.pack(side='left')
        self.market_box.pack(side='left')
        self.scroll_market.pack(side='left', fill='y')
        self.ent.bind('<Return>', self.insert_box)
        self.market_box.bind('<Double-Button-1>', self.insert_ent)

    def insert_box(self, event):
        if self.ent.get():
            self.market_box.insert(tk.END, self.ent.get())
            self.ent.delete(0, tk.END)

    def insert_ent(self, event):
        self.ent.delete(0, tk.END)
        self.ent.insert(0, self.market_box.get(self.market_box.curselection()))


if __name__ == '__main__':
    root = Events()
    root.mainloop()