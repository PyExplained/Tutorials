from tkinter import *
import time
import math

angle = 0
radius = 100
x_speed = 1
sleep_time = 0.005

width = 700
height = 700

tk = Tk()
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

lines = []
while True:
    radians = angle * math.pi / 180
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    triangle = canvas.create_polygon([(width / 2, height / 2), (width / 2 + x, height / 2 + y),
                                      (width / 2 + x, height / 2)], fill='', outline='black', width=2)
    if angle <= 360 and angle >= 1:
        canvas.create_line([(width / 2 + prev_x, height / 2 + prev_y), (width / 2 + x, height / 2 + y)],
                           fill='red', width=2)
    for i, line in enumerate(lines):
        if canvas.coords(line)[0] > width:
            canvas.delete(line)
            del lines[i]
        else:
            canvas.move(line, x_speed, 0)

    if angle >= 1:
        connection_line = canvas.create_line([(width / 2 + radius, height / 2 + prev_y),
                                              ((width / 2 + x, height / 2 + y))], fill='blue')
        line = canvas.create_line([(width / 2 + radius, height / 2 + prev_y),
                                   (width / 2 + radius + x_speed, height / 2 + y)], fill='green')
        lines.append(line)

    tk.update()
    time.sleep(sleep_time)

    canvas.delete(triangle)
    if angle >= 1:
        canvas.delete(connection_line)

    angle += 1
    prev_x = x
    prev_y = y