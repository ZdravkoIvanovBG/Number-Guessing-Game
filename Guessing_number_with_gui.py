import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import random

random_number = random.randint(1, 100)
tries = 3

root = Tk()
root.geometry("600x500")
root.title("Lottery")

lbl = Label(root, text="Number Guessing Game!", font=("Arial", 16), fg="green")
lbl.pack(pady=15)

enter_number = Entry(root)
enter_number.pack(pady=5)


def click():
    global random_number
    global tries

    if int(enter_number.get()) == random_number:
        messagebox.showinfo(title="Lottery", message="You won the Lottery! Woohoo!")
        exit()

    if tries <= 1:
        messagebox.showinfo(title="Lottery", message="You don't have any more tries!")
        exit()

    else:
        tries -= 1

        if tries == 2:
            messagebox.showinfo(title="Lottery",
                                message=f"You didn't win the Lottery! But don't worry you have {tries} try left.")
        else:
            messagebox.showinfo(title="Lottery",
                                message=f"You didn't win the Lottery! But don't worry you have {tries} tries left.")


btn = Button(root, text="Check Number", font=("Arial", 16), command=click)
btn.pack(pady=15)

root.mainloop()
