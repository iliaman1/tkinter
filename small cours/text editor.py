import tkinter as tk


class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('text editor')
        self.geometry('640x480')
        self.iconphoto(False, tk.PhotoImage(file='img/book.png'))

        self.top_frame = tk.LabelFrame(text='File options')
        self.bot_frame = tk.LabelFrame(text='Edit')
        self.ent = tk.Entry(self.top_frame, width=20, font=("Times New Roman", 14, "bold"))
        self.but_open = tk.Button(self.top_frame, text="Open", font=("Times New Roman", 14, "bold"),
                                  command=self.open_file)
        self.but_save = tk.Button(self.top_frame, text="Save", font=("Times New Roman", 14, "bold"),
                                  command=self.save_file)
        self.text_area = tk.Text(self.bot_frame, width=20, height=20)
        self.scroll = tk.Scrollbar(self.bot_frame, command=self.text_area.yview)

        self.top_frame.pack(fill='x', expand=True)
        self.bot_frame.pack(fill='both', expand=True)
        self.ent.pack(side='left', fill='x', expand=True, padx=10)
        self.but_open.pack(side='left', padx=5, pady=5)
        self.but_save.pack(side='left', padx=5, pady=5)
        self.text_area.pack(side='left', fill='both', expand=True)
        self.scroll.pack(side='left', fill='y')

        self.text_area.config(yscrollcommand=self.scroll.set)

    def open_file(self):
        try:
            with open(f"files/{self.ent.get()}", 'r') as fp:
                self.text_area.insert(0.0, fp.read())
        except Exception:
            self.ent.delete(0, tk.END)
            self.ent.insert(0, "Произошла какая-то ошибка!")

    def save_file(self):
        try:
            with open(f"files/{self.ent.get()}", 'w') as fp:
                fp.write(self.text_area.get(0.0, 'end'))
        except Exception:
            self.ent.delete(0, tk.END)
            self.ent.insert(0, "Произошла какая-то ошибка!")


if __name__ == '__main__':
    root = TextEditor()
    root.mainloop()
