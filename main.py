from tkinter import *
import random

window = Tk()
window.title("Rolling Dice")
window.minsize(300,150)
window.maxsize(700,400)
window.config(bg="yellow")

dice_image = PhotoImage(file="Icons/dice.png")

def roll(event=None):
    label_1["text"] = random.randint(1,6)

window.rowconfigure([0,1], weight=1)
window.columnconfigure(0, weight=1)

button_1 = Button(master=window, text="Click or Enter to Roll", font="Arial 15", command=roll, bg="green", fg="white", padx=10, pady=10, borderwidth=5, compound=RIGHT, image=dice_image)
button_1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
window.bind('<Return>', roll)

label_1 = Label(master=window, bg="yellow", font="Arial 18")
label_1.grid(row=1, column=0, padx=10, pady=20)

window.mainloop()
