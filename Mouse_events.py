from tkinter import *


def mouse_event(event):
    print("You clicked mouse on " + str(event.x) + "," + str(event.y))


def motion_event(event):
    print("current cursor position: " + str(event.x) + "," + str(event.y))


window = Tk()

window.bind("<Button-1>", mouse_event)   # left mouse click
window.bind("<Button-2>", mouse_event)   # scroll wheel
window.bind("<Button-3>", mouse_event)   # right mouse click
window.bind("<ButtonRelease>", mouse_event)   # says when mouse button was released
window.bind("<Enter>", mouse_event)   # says when window was entered by cursor
window.bind("<Leave>", mouse_event)   # says when window was leaved by cursor
window.bind("<Motion>", motion_event)

window.mainloop()
