import tkinter as tk


class ContactList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('contact list')
        self.geometry('320x240')
        self.iconphoto(False, tk.PhotoImage(file='img/book.png'))

        self.left_frame = tk.LabelFrame(text='Contacts')
        self.right_frame = tk.LabelFrame(text='telephone number')
        self.label = tk.Label(self.right_frame, text='select target')
        self.var = tk.IntVar()
        self.var.set(-1)
        self.contact1 = tk.Radiobutton(self.left_frame,
                                       variable=self.var,
                                       value=0,
                                       text='Андрей уже не Дорошенко',
                                       command=self.show_number,
                                       indicatoron=False)
        self.contact2 = tk.Radiobutton(self.left_frame,
                                       variable=self.var,
                                       value=1,
                                       text='Федеральный',
                                       command=self.show_number,
                                       indicatoron=False)
        self.contact3 = tk.Radiobutton(self.left_frame,
                                       variable=self.var,
                                       value=2,
                                       text='Я(на всякий)',
                                       command=self.show_number,
                                       indicatoron=False)

        self.left_frame.pack(side='left', fill='y', expand=True)
        self.right_frame.pack(side='left', fill='y', expand=True)
        self.contact1.pack(anchor=tk.W, fill='x')
        self.contact2.pack(anchor=tk.W, fill='x')
        self.contact3.pack(anchor=tk.W, fill='x')
        self.label.pack(expand=1)

    def show_number(self):
        if self.var.get() == 0:
            self.label['text'] = '+370(648)77720'
        elif self.var.get() == 1:
            self.label['text'] = '+375(25)1021022'
        elif self.var.get() == 2:
            self.label['text'] = '+375(25)5226348'


if __name__ == '__main__':
    root = ContactList()
    root.mainloop()
