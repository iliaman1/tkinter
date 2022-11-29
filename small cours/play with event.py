import tkinter as tk


class Events(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('play with event')
        self.geometry('320x240')
        self.iconphoto(False, tk.PhotoImage(file='img/event.png'))

        self.top_frame = tk.LabelFrame(text='control menu')
        self.top_left_frame = tk.Frame(self.top_frame)
        self.top_right_frame = tk.Frame(self.top_frame)
        self.bot_frame = tk.LabelFrame(text='text place')
        self.ent1 = tk.Entry(self.top_left_frame)
        self.ent2 = tk.Entry(self.top_left_frame)
        self.btn_change = tk.Button(self.top_right_frame, text='Change', command=self.but_change_text_size)
        self.text = tk.Text(self.bot_frame, bg='lightgrey')

        self.top_frame.pack(fill='x')
        self.bot_frame.pack(fill='both')
        self.top_left_frame.pack(side='left')
        self.top_right_frame.pack(side='left')
        self.ent1.pack()
        self.ent2.pack()
        self.btn_change.pack()
        self.text.pack()
        self.text.bind('<FocusIn>', self.focus_text)
        self.text.bind('<FocusOut>', self.focus_text)
        self.ent1.bind('<Return>', self.change_text_size)
        self.ent2.bind('<Return>', self.change_text_size)

    def focus_text(self, event):
        if event.type == '9':
            event.widget['bg'] = 'white'
        elif event.type == '10':
            event.widget['bg'] = 'lightgrey'

    def change_text_size(self, event):
        if num1 := self.ent1.get():
            if num2 := self.ent2.get():
                self.text['width'] = num1
                self.text['height'] = num2

    def but_change_text_size(self):
        if num1 := self.ent1.get():
            if num2 := self.ent2.get():
                self.text['width'] = num1
                self.text['height'] = num2


if __name__ == '__main__':
    root = Events()
    root.mainloop()
