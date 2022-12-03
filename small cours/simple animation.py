import tkinter as tk
from PIL import Image, ImageTk


class MyAnimation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple game')
        self.geometry('300x200')
        self.iconphoto(False, tk.PhotoImage(file='img/animation.png'))
        self.config(cursor='man')

        self.canva = tk.Canvas(width=300, height=200, bg="white")
        self.scaled_dog = Image.open('img/happy_dog.png').resize((40, 40))
        self.dog = ImageTk.PhotoImage(self.scaled_dog)
        self.dog_tk = self.canva.create_image(10, 10, anchor='nw', image=self.dog)

        self.canva.pack()

        self.canva.bind('<Button-1>', self.motion)

    def motion(self, event):
        if self.canva.coords(self.dog_tk)[0] < event.x:
            self.canva.move(self.dog_tk, 1, 0)
        if self.canva.coords(self.dog_tk)[1] < event.y:
            self.canva.move(self.dog_tk, 0, 1)
        if self.canva.coords(self.dog_tk)[0] > event.x:
            self.canva.move(self.dog_tk, -1, 0)
        if self.canva.coords(self.dog_tk)[1] > event.y:
            self.canva.move(self.dog_tk, 0, -1)
        if event.x != self.canva.coords(self.dog_tk)[0] or event.y != self.canva.coords(self.dog_tk)[1]:
            self.after(10, self.motion, event)


if __name__ == '__main__':
    root = MyAnimation()
    root.mainloop()
