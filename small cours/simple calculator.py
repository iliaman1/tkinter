import tkinter as tk


class Block(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple calculator')
        self.geometry('400x500')
        self.iconphoto(False, tk.PhotoImage(file='img/calcul.png'))
        self.ent = tk.Entry(width=20, font=("Helvetica", 15, "bold"))
        self.ent2 = tk.Entry(width=20, font=("Helvetica", 15, "bold"))
        self.but_add = tk.Button(text="+", font=("Helvetica", 15, "bold"), command=self.add)
        self.but_sub = tk.Button(text="-", font=("Helvetica", 15, "bold"), command=self.sub)
        self.but_mul = tk.Button(text="*", font=("Helvetica", 15, "bold"), command=self.mul)
        self.but_div = tk.Button(text="/", font=("Helvetica", 15, "bold"), command=self.div)
        self.but_cls = tk.Button(text="clear", font=("Helvetica", 15, "bold"), command=self.clear)
        self.lab = tk.Label(width=20, font=("Helvetica", 15, "bold"), bg='black', fg='white')

        self.ent.pack(fill='both', expand=True)
        self.ent2.pack(fill='both', expand=True)
        self.but_add.pack(fill='both', expand=True)
        self.but_sub.pack(fill='both', expand=True)
        self.but_mul.pack(fill='both', expand=True)
        self.but_div.pack(fill='both', expand=True)
        self.but_cls.pack(fill='both', expand=True)
        self.lab.pack(fill='both', expand=True)

    def get_numbas(self):
        try:
            first_numba = float(self.ent.get())
            second_numba = float(self.ent2.get())
        except:
            self.lab['foreground'] = 'red'
            self.lab['text'] = 'ОШИБКА'
        else:
            self.lab['foreground'] = 'white'
            return first_numba, second_numba

    def add(self):
        if self.get_numbas():
            self.lab['text'] = str(self.get_numbas()[0] + self.get_numbas()[1])

    def sub(self):
        if self.get_numbas():
            self.lab['text'] = str(self.get_numbas()[0] - self.get_numbas()[1])

    def mul(self):
        if self.get_numbas():
            self.lab['text'] = str(self.get_numbas()[0] * self.get_numbas()[1])

    def div(self):
        if self.get_numbas():
            try:
                self.lab['text'] = str(self.get_numbas()[0] / self.get_numbas()[1])
            except ZeroDivisionError:
                self.lab['foreground'] = 'red'
                self.lab['text'] = 'ОШИБКА ДЕЛЕНИЕ НА НОЛЬ!!'

    def clear(self):
        self.ent.delete("0", tk.END)
        self.ent2.delete("0", tk.END)


if __name__ == '__main__':
    root = Block()

    root.mainloop()
