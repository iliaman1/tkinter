import tkinter as tk


class Color:
    RED = '#FF0000'
    ORANGE = '#FFA500'
    YELLOW = '#FFFF00'
    GREEN = '#008000'
    LIGHT_BLUE = '#ADD8E6'
    BLUE = '#0000FF'
    VIOLET = '#EE82EE'
    BLACK = 'black'
    WHITE = 'white'
    GRAY = '#808080'


class Theme:
    name = "default"
    geometry = '400x500'
    font = ("Lucida Console", 20, "bold")
    main_color = Color.VIOLET
    label = dict(width=20, font=font, bg=Color.WHITE, fg=Color.BLACK)
    button = dict(font=font)
    entry = dict(width=20, font=font, bg=Color.WHITE, fg=Color.BLACK)
    pack = dict(fill='both', expand=True)


class DarkHorizont(Theme):
    name = "dark horizont"
    geometry = '500x235'
    font = ("Helvetica", 15, "bold")
    main_color = Color.VIOLET
    label = dict(width=20, font=font, bg=Color.BLACK, fg=Color.GREEN)
    button = dict(font=font)
    entry = dict(width=20, font=font, bg=Color.BLACK, fg=Color.GREEN)
    pack = dict(side='left', padx=10, pady=10, fill='both', expand=True)


class Palette(tk.Tk):
    def __init__(self, theme: Theme = Theme()):
        super().__init__()
        self.theme = theme
        self.title('simple palette (' + self.theme.name + ')')
        self.geometry(self.theme.geometry)
        self.configure(bg=self.theme.main_color)
        self.iconphoto(False, tk.PhotoImage(file='img/color-palette.png'))

        self.lab = tk.Label(**self.theme.label)
        self.entry = tk.Entry(**self.theme.entry)
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
        self.but_red.pack(**self.theme.pack)
        self.but_orange.pack(**self.theme.pack)
        self.but_yellow.pack(**self.theme.pack)
        self.but_green.pack(**self.theme.pack)
        self.but_light_blue.pack(**self.theme.pack)
        self.but_blue.pack(**self.theme.pack)
        self.but_violet.pack(**self.theme.pack)

    def get_color(self, color_hex: str, color: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, color_hex)
        self.lab['text'] = color
        self.lab['fg'] = color_hex


if __name__ == '__main__':
    root = Palette(DarkHorizont())

    root.mainloop()
