import tkinter as tk


class Color:
    RED = '#FF0000'
    ORANGE = '#FFA500'
    YELLOW = '#FFFF00'
    GREEN = '#008000'
    LIGHT_BLUE = '#ADD8E6'
    BLUE = '#0000FF'
    VIOLET = '#EE82EE'


class Palette(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple palette')
        self.geometry('400x500')
        self.iconphoto(False, tk.PhotoImage(file='img/color-palette.png'))

        self.lab = tk.Label(width=20, font=("Helvetica", 15, "bold"), bg='black', fg='white')
        self.entry = tk.Entry(width=20, font=("Helvetica", 15, "bold"))
        self.but_red = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.RED,
                                 command=lambda: self.get_color(Color.RED, 'red'))
        self.but_orange = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.ORANGE,
                                    command=lambda: self.get_color(Color.ORANGE, 'orange'))
        self.but_yellow = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.YELLOW,
                                    command=lambda: self.get_color(Color.YELLOW, 'yellow'))
        self.but_green = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.GREEN,
                                   command=lambda: self.get_color(Color.GREEN, 'green'))
        self.but_light_blue = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.LIGHT_BLUE,
                                        command=lambda: self.get_color(Color.LIGHT_BLUE, 'light blue'))
        self.but_blue = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.BLUE,
                                  command=lambda: self.get_color(Color.BLUE, 'blue'))
        self.but_violet = tk.Button(text="", font=("Helvetica", 15, "bold"), bg=Color.VIOLET,
                                    command=lambda: self.get_color(Color.VIOLET, 'violet'))

        self.lab.pack(fill='both', expand=True)
        self.entry.pack(fill='both', expand=True)
        self.but_red.pack(fill='both', expand=True)
        self.but_orange.pack(fill='both', expand=True)
        self.but_yellow.pack(fill='both', expand=True)
        self.but_green.pack(fill='both', expand=True)
        self.but_light_blue.pack(fill='both', expand=True)
        self.but_blue.pack(fill='both', expand=True)
        self.but_violet.pack(fill='both', expand=True)

    def get_color(self, color_hex: str, color: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, color_hex)
        self.lab['text'] = color
        self.lab['fg'] = color_hex


if __name__ == '__main__':
    root = Palette()

    root.mainloop()
