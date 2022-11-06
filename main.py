from tkinter import *

window = Tk()
window.title("Euro-jackpot")
window.geometry("500x500")

label = Label(window,
              text="Euro-jackpot",
              font=("Constantia", 30),)
label.grid(row=0, column=0, columnspan=7, pady=10)

entry1 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry1.grid(row=1, column=1, padx=10)

entry2 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry2.grid(row=1, column=2, padx=10)

entry3 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry3.grid(row=1, column=3, padx=10)

entry4 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry4.grid(row=1, column=4, padx=10)

entry5 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry5.grid(row=1, column=5, padx=10)

entry6 = Entry(window,
               font=("Constantia", 25),
               width=3,
               borderwidth=3
               )
entry6.grid(row=1, column=6, padx=10)

submit = Button(window,
                text="Submit",
                font=("Constantia", 15),
                borderwidth=3,
                )
submit.grid(row=2, column=0, columnspan=7, pady=10)

window.mainloop()
