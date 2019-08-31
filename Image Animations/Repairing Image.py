from tkinter import *
from random import randint
import cv2
import time

resolution = 0.1  # 1 = full

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# Insert file path below
img = cv2.imread(r'filepath')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = len(img[0])
height = len(img)


class Pixel:
    def __init__(self, canvas, x, y, c, w, h, tx, ty):
        self.canvas = canvas
        self.color = c
        self.x = x
        self.y = y
        self.target_x = tx
        self.target_y = ty
        hexa = '#{:02x}{:02x}{:02x}'.format(c[0], c[1], c[2])
        
        self.body = self.canvas.create_rectangle(self.x, self.y, self.x+w, self.y+h, fill=hexa, outline='')
    def move(self):
        x_off = self.target_x - self.x
        y_off = self.target_y - self.y

        if -4 <= x_off <= 4 or -4 <= y_off <= 4:
            self.canvas.move(self.body, x_off, y_off)
            self.x += x_off
            self.y += y_off
            
        self.canvas.move(self.body, x_off/25, y_off/25)
        self.x += x_off/25
        self.y += y_off/25

pixels = []
tk.update()
w = canvas.winfo_width() / (2 * width * resolution)
h = canvas.winfo_height() / (2 * height * resolution)

yy = 0
for y in range(0, height, round(1/resolution)):
    yy += 1
    xx = 0
    for x in range(0, width, round(1/resolution)):
        p = Pixel(canvas, randint(0, canvas.winfo_width()), randint(0, canvas.winfo_height()), img[y][x], w, h, 125+xx*w, 125+yy*h)
        #p = Pixel(canvas, 125 + xx * w, 125 + yy * h, img[y][x], w, h,
                            # randint(0, canvas.winfo_width()), randint(0, canvas.winfo_height()))
        pixels.append(p)
        xx += 1

while True:
    try:
        tk.update()
        for particle in pixels:
            particle.move()
        time.sleep(0.01)
    except:
        break