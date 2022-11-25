import tkinter as tk
from math import pow, log


class Color:
    RED = 'red'
    WHITE = 'white'
    BLACK = 'black'


class Error:
    ZERO_DIVISION = 'Stop zero division blyat!!'
    WRONG_NUMBER = 'Incorrect numer/s beach!!'


class Calculator(tk.Tk):
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
        self.but_pow = tk.Button(text="pow", font=("Helvetica", 15, "bold"), command=self.pow)
        self.but_log = tk.Button(text="log", font=("Helvetica", 15, "bold"), command=self.log)
        self.but_cls = tk.Button(text="clear", font=("Helvetica", 15, "bold"), command=self.clear)
        self.lab = tk.Label(width=20, font=("Helvetica", 15, "bold"), bg=Color.BLACK, fg=Color.WHITE)

        self.ent.pack(fill='both', expand=True)
        self.ent2.pack(fill='both', expand=True)
        self.but_add.pack(fill='both', expand=True)
        self.but_sub.pack(fill='both', expand=True)
        self.but_mul.pack(fill='both', expand=True)
        self.but_div.pack(fill='both', expand=True)
        self.but_pow.pack(fill='both', expand=True)
        self.but_log.pack(fill='both', expand=True)
        self.but_cls.pack(fill='both', expand=True)
        self.lab.pack(fill='both', expand=True)

    def get_numbas(self) -> tuple[float, float]:  # optional
        self.lab['foreground'] = Color.WHITE

        try:
            return float(self.ent.get()), float(self.ent2.get())
        except ValueError:
            self.lab['foreground'] = Color.RED
            self.lab['text'] = Error.WRONG_NUMBER

    def add(self):
        if number := self.get_numbas():
            self.lab['text'] = str(number[0] + number[1])

    def sub(self):
        if number := self.get_numbas():
            self.lab['text'] = str(number[0] - number[1])

    def mul(self):
        if number := self.get_numbas():
            self.lab['text'] = str(number[0] * number[1])

    def div(self):
        if number := self.get_numbas():
            try:
                self.lab['text'] = str(number[0] / number[1])
            except ZeroDivisionError:
                self.lab['foreground'] = Color.RED
                self.lab['text'] = Error.ZERO_DIVISION

    def pow(self):
        if number := self.get_numbas():
            self.lab['text'] = str(pow(number[0], number[1]))

    def log(self):
        if number := self.get_numbas():
            self.lab['text'] = str(log(number[0], number[1]))

    def clear(self):
        self.ent.delete("0", tk.END)
        self.ent2.delete("0", tk.END)


if __name__ == '__main__':
    root = Calculator()

    root.mainloop()
