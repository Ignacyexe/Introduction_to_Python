from tkinter import *

window = Tk()
window.geometry("425x140")


def submit():
    label = Label(window,
                  text="You choose " + str(scale.get()) + " points out of 10, thanks for opinion!",
                  font=("Consolas", 11)
                  )
    window.after(1500, lambda: label.destroy())
    label.pack()


rate = Label(window,
             text="Rate our product, this helps us alot! :)",
             font=("Consolas", 14))
rate.pack(side=TOP)

scale = Scale(window,
              from_=0,
              to=10,
              length=250,
              orient=HORIZONTAL,
              font=("Consolas", 12),
              tickinterval=1,   # adds numeric indicators to the value
              resolution=1
              )
scale.pack()

button = Button(window,
                text="Submit",
                font=("Consolas", 10),
                command=submit,
                )
button.pack()

window.mainloop()
