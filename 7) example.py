import tkinter as tk

def increase():
    value = int(label["text"])
    label["text"]=f"{value+1}"

def decrease():
    value=int(label["text"])
    label["text"]=f"{value-1}"

    
window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0,1,2], minsize=50)

btn1= tk.Button(master=window, text="-", command=decrease)
btn1.grid(row=0, column=0, sticky="nsew")

label = tk.Label(master=window, text="0")
label.grid(row=0, column=1)

btn2= tk.Button(master=window, text="+", command=increase)
btn2.grid(row=0, column=2, sticky= "nsew")


window.mainloop()
