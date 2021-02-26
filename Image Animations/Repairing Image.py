import PIL.Image, PIL.ImageTk
from random import randint
from tkinter import *
import numpy as np
import time
import cv2

resolution = 0.1  # 1 = full
speed = 1
win_width = 1280
win_height = 720

tk = Tk()
canvas = Canvas(tk, width=win_width, height=win_height)
canvas.pack()

# Insert file path below
img = cv2.imread(r'C:\Users\manud\OneDrive\Bureaublad\test_img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = len(img[0])
height = len(img)


class Pixel:
    def __init__(self, x, y, c, s, tx, ty):
        self.color = c
        self.x = x
        self.y = y
        self.target_x = tx
        self.target_y = ty
        self.size = s

    def move(self):
        x_off = self.target_x - self.x
        y_off = self.target_y - self.y

        if abs(x_off) + abs(y_off) < 2:
            self.x += x_off
            self.y += y_off
        else:
            self.x += x_off / (1/speed) * delta_time
            self.y += y_off / (1/speed) * delta_time

pixels = []
if width > height:
    s = win_width / (2 * width * resolution)
    im_w = win_width / 2
    im_h = height / width * im_w
else:
    s = win_height / (2 * height * resolution)
    im_h = win_height / 2
    im_w = width / height * im_h

yy = 0
for y in range(0, height, round(1/resolution)):
    yy += 1
    xx = 0
    for x in range(0, width, round(1/resolution)):
        p = Pixel(randint(0, win_width), randint(0, win_height), img[y][x], s,
                  win_width/2-im_w/2+xx*s, win_height/2-im_h/2+yy*s)
        # p = Pixel(win_width/2-im_w/2+xx*w, win_height/2-im_h/2+yy*h, img[y][x], w, h,
        #                     randint(0, win_width), randint(0, win_height))
        pixels.append(p)
        xx += 1

last_time = time.time()
delta_time = 0.07
while True:
    canvas.delete('all')
    image = np.full((win_height, win_width, 3), 228)

    for particle in pixels:
        particle.move()
        image[int(particle.y):int(particle.y + particle.size),
        int(particle.x):int(particle.x + particle.size)] = particle.color

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(image.astype(np.uint8)))
    canvas.create_image(0, 0, image=photo, anchor=NW)
    tk.update()

    delta_time = time.time() - last_time
    last_time = time.time()
