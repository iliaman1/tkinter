import tkinter as tk
from PIL import Image, ImageTk


class MyAnimation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple game next story')
        self.iconphoto(False, tk.PhotoImage(file='img/animation.png'))

        self.canva = tk.Canvas(width=300, height=200, bg="white").pack()
        tk.Button(text="units settings", width=20, command=self.setting).pack()

    def setting(self):
        SettingWindow().mainloop()


class SettingWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('units settings')

        self.top_frame = tk.LabelFrame(text='top')
        self.top_top_frame = tk.LabelFrame(self.top_frame, text='top top').pack()
        self.top_bot_frame = tk.LabelFrame(self.top_frame, text='top bot').pack()
        self.x1_label = tk.Label(self.top_top_frame, text='x1=').pack(side='left')
        self.x1_edit = tk.Entry(self.top_top_frame).pack(side='left')
        self.y1_label = tk.Label(self.top_top_frame, text='y1=').pack(side='left')
        self.y1_edit = tk.Entry(self.top_top_frame).pack(side='left')
        self.x2_label = tk.Label(self.top_bot_frame, text='x2=').pack(side='left')
        self.x2_edit = tk.Entry(self.top_bot_frame).pack(side='left')
        self.y2_label = tk.Label(self.top_bot_frame, text='y2=').pack(side='left')
        self.y2_edit = tk.Entry(self.top_bot_frame).pack(side='left')
        self.var = tk.IntVar()
        self.var.set(-1)
        self.dog = tk.Radiobutton(variable=self.var,
                                  value=0,
                                  text='Собакен',
                                  indicatoron=False)
        self.cat = tk.Radiobutton(variable=self.var,
                                  value=1,
                                  text='Китик',
                                  indicatoron=False)
        self.penguin = tk.Radiobutton(variable=self.var,
                                      value=2,
                                      text='Пинг?',
                                      indicatoron=False)


if __name__ == '__main__':
    root = MyAnimation()
    root.mainloop()
