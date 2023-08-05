import tkinter as tk
from tkinter import ttk

def chk_btn_clicked():
    # for every checkbox, there will be if, else condition 
    if chk_btn_1_var.get():
        print("Checkbutton 1 is selected")
    else:
        print("Checkbutton 1 is deselected")

    if chk_btn_2_var.get():
            print("Checkbutton 2 is selected")
    else:
        print("Checkbutton 2 is deselected")
    

# main
window = tk.Tk()
window.title("Check button")

pad={"padx": 40, "pady": 15} # padding


# chk_btn_var.set(0)  # Setting the initial checkbutton state

chk_btn_1_var = tk.IntVar() # Creating a variable to store the checkbutton state
chk_btn_1 = ttk.Checkbutton(window, text="Option 1", variable=chk_btn_1_var, command=chk_btn_clicked)
chk_btn_1.pack(**pad)

chk_btn_2_var = tk.IntVar() # Creating a variable to store the checkbutton state
chk_btn_2 = ttk.Checkbutton(window, text="Option 2", variable=chk_btn_2_var, command=chk_btn_clicked)
chk_btn_2.pack(**pad)


window.mainloop()