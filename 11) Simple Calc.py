import tkinter as tk

window = tk.Tk()
window.title("Utility-1")
window.resizable(False, False)

# Arithmetic Calculation
def btn1_pressed():
    def evaluate():
        value=eval(entry.get())
        label1A["text"]=str(value)

    new_win1=tk.Toplevel() # to create new window
    new_win1.title("Arithmetic Calculator")
    new_win1.resizable(False, False)
    new_win1.focus()  #To focus on the new window by default

    entry=tk.Entry(master=new_win1, width=20)
    entry.grid(row=0, column=0, padx=25, pady=25)

    btn1A=tk.Button(master=new_win1, text="=", relief="groove", command=evaluate)
    btn1A.grid(row=0, column=1, padx=10, pady=25)

    label1A=tk.Label(master=new_win1, text="")
    label1A.grid(row=0, column=2, padx=10, pady=25)


arithmetic_btn=tk.Button(master=window, relief="groove", text="Arithmetic Calculator", command=btn1_pressed)
arithmetic_btn.grid(row=0, column=0, padx=25, pady=25)

window.mainloop()