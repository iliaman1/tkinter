import tkinter as tk


class MyAnimation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple game')
        self.geometry('300x200')
        self.iconphoto(False, tk.PhotoImage(file='img/animation.png'))

        self.canva = tk.Canvas(width=300, height=200, bg="white")
        self.ball = self.canva.create_oval(0, 100, 40, 140, fill='green')

        self.canva.pack()

        self.canva.bind('<Button-1>', self.motion)

    def motion(self, event):
        while event.x != self.canva.coords(self.ball)[2] or event.y != self.canva.coords(self.ball)[3]:
            if self.canva.coords(self.ball)[2] < event.x:
                self.canva.move(self.ball, 1, 0)
            if self.canva.coords(self.ball)[3] < event.y:
                self.canva.move(self.ball, 0, 1)
            if self.canva.coords(self.ball)[2] > event.x:
                self.canva.move(self.ball, -1, 0)
            if self.canva.coords(self.ball)[3] > event.y:
                self.canva.move(self.ball, 0, -1)

        # if self.canva.coords(self.ball)[2]<300:
        #     self.after(10, self.motion(event))


if __name__ == '__main__':
    root = MyAnimation()
    root.mainloop()
