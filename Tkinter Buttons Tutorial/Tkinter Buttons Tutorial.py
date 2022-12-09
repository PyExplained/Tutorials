from tkinter import *

tk = Tk()
tk.geometry('300x300')

def press(_):
    b.config(image=photo_2)
    print('pressed')

def release(_):
    b.config(image=photo_1)
    print('released')

photo_1 = PhotoImage(file='button.gif').subsample(2, 2)
photo_2 = PhotoImage(file='button_2.gif').subsample(2, 2)

b = Button(tk, image=photo_1, cursor='hand2', border='0')
b.place(x=150, y=150, anchor=CENTER)

b.bind('<ButtonPress>', press)
b.bind('<ButtonRelease>', release)

tk.mainloop()
