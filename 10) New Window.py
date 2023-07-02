import tkinter as tk

window = tk.Tk()
window.title("Scrap")
window.resizable(False, False)


def btn1_pressed():
    new_window_1=tk.Toplevel() # to create new window
    new_window_1.title("Window 2")
    new_window_1.resizable(False, False)
    new_window_1.focus()  #To focus on the new window by default

    """ contents of the new window should be here """
    label1=tk.Label(master=new_window_1,text="Popped-up new Window")
    label1.pack(padx=25, pady=25)


btn1=tk.Button(master=window, relief="groove", text="Button 1", command=btn1_pressed)
btn1.grid(row=0, column=0, padx=25, pady=25)

window.mainloop()