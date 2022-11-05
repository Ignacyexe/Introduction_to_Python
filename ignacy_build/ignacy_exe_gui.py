from tkinter import *
from PIL import ImageTk, Image

# widgets - GUI elements: buttons, textboxes, labels, images
# windows - serves as a container to hold or contain these widgets

window = Tk()   # instantiate an instance of a window
# window.geometry("800x600")
window.title("Ignacy.exe demo.gui_version")

icon = PhotoImage(file="Ignacy.exe.png")

# resizing button image with Pillow package
picture = Image.open("more.gif")
resized = picture.resize((525, 135), Image.ANTIALIAS)
button_photo = ImageTk.PhotoImage(resized)

window.iconphoto(True, icon)

window.config(background="black")

label = Label(window,
              text="Ignacy.exe",
              font=("Constantia", 40, "normal"),
              fg="red",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=10,
              pady=5,
              image=icon,
              compound='bottom'
              )
label.pack()
# label.place(x=0, y=0)

count = 0


def click():
    print("You clicked the button!")
    global count
    count += 1
    print(count)


button = Button(window,
                text="click me!",
                command=click,
                font=("Constantia", 16),
                fg="red",
                bg="black",
                activebackground="black",
                activeforeground="red",
                state=ACTIVE,
                image=button_photo,
                compound="bottom")
button.pack()

window.mainloop()   # place window on computer screen, listens to events
