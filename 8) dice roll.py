import random
import tkinter as tk

def roll():
    # we can use any of the method
    label["text"] = str(random.randint(1, 6))
    # label["text"] = f"{random.randint(1,6)}"

window=tk.Tk()

window.rowconfigure([0,1], minsize=10)
window.columnconfigure(0, minsize=10)

btn1=tk.Button(master=window, text="Roll", width=20, height=3, command=roll, relief="ridge", bg="#E3F4F4")
btn1.grid(row=0, column=0, sticky="ew")

label=tk.Label(master=window, text="", width=20, height=3, bg="#D2E9E9")
label.grid(row=1, column=0, sticky="ew")


window.mainloop()


