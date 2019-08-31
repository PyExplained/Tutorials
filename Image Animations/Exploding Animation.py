from tkinter import *
import cv2
import time
# from math import *
from random import uniform

resolution = 0.1

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# Insert file path below
img = cv2.imread('filepath')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = len(img[0])
height = len(img)


class Pixel:
    def __init__(self, canvas, x, y, c, w, h):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ground = False
        self.vel_x = 0
        self.vel_y = 0
        self.fric = 0.75
        self.gravity = 20
        hexa = '#{:02x}{:02x}{:02x}'.format(c[0], c[1], c[2])

        self.body = self.canvas.create_rectangle(125+x-w/2, 125+y-h/2, 125+x+w/2, 125+y+h/2, fill=hexa, outline='')
    def calc(self):
        global pixels

        self.ground = False
        # (here I was toying around a bit)
        # for p in pixels:
        #     if p == self:
        #         continue
        #     if (self.vel_x < 0 and self.pos[0] + self.vel_x <= p.pos[2] and self.pos[2] >= p.pos[0]) or \
        #             (self.vel_x > 0 and self.pos[0] >= p.pos[0] and self.pos[2] + self.vel_x <= p.pos[0]):
        #         temp = self.vel_x
        #         self.vel_x = p.vel_x
        #         p.calcul = True
        #         p.vel_x = temp
        #     if (self.pos[1] + self.vel_y < p.pos[3] + p.vel_y and self.pos[3] > p.pos[1] + p.vel_y) and \
        #             (self.pos[2] + self.vel_x > p.pos[0] + p.vel_x and self.pos[0] + p.vel_x > p.pos[2] + self.vel_x):
        #     if sqrt((self.pos[0] + self.vel_x + self.w/2 - (p.pos[0] + p.vel_x + p.w/2)) ** 2 + (
        #             (self.pos[1] + self.vel_y + self.h/2 - (p.pos[1] + p.vel_y + p.h/2)) ** 2)) <= self.h:
        #         if p.ground:
        #             self.ground = True
        #             self.y_vel = p.pos[1] - self.pos[3]
        #             self.x_vel = 0

        if not self.ground:
            self.pos = self.canvas.coords(self.body)

            self.vel_x *= self.fric
            self.vel_y *= self.fric

            self.vel_y += self.gravity
            if self.pos[2] + self.vel_x >= self.canvas.winfo_width():
                self.vel_x = self.canvas.winfo_width() - self.pos[2] - self.w
            elif self.pos[0] + self.vel_x <= 0:
                self.vel_x = self.canvas.winfo_width() - self.pos[0]
            if self.pos[3] + self.vel_y >= self.canvas.winfo_height():
                self.vel_y = self.canvas.winfo_height() - self.pos[3] - self.h
                self.ground = True
                self.vel_x = 0
        else:
            self.vel_x = 0
            self.vel_y = 0

    def explode(self):
        self.pos = self.canvas.coords(self.body)
        x = self.pos[0] - canvas.winfo_width() / 2
        y = self.pos[1] - canvas.winfo_height() / 2
        self.vel_x = uniform(x-2, x+2) / 2
        if y > 0:
            self.vel_y = uniform(y-2, y+2)
        else:
            self.vel_y = uniform(y - 2, y + 20)
    def move(self):
        self.canvas.move(self.body, self.vel_x, self.vel_y)


pixels = []
tk.update()
w = canvas.winfo_width() / (2 * width * resolution)
h = canvas.winfo_height() / (2 * height * resolution)

yy = -1
for y in range(0, height, round(1/resolution)):
    yy += 1
    xx = 0
    for x in range(0, width, round(1/resolution)):
        xx += 1
        p = Pixel(canvas, xx*w, yy*h, img[y][x], w, h)
        pixels.append(p)

tk.update()
time.sleep(2)

for pixel in pixels:
    pixel.explode()

while True:
    try:
        for p in range(len(pixels)-1, -1, -1):
            pixels[p].calc()
        for p in pixels:
            p.move()
        tk.update()
        time.sleep(0.01)
    except:
        break
