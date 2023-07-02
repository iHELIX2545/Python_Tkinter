import tkinter as tk

def convert_c():
    value=entry.get()
    value= (5 / 9) * (float(value) - 32)
    label_c["text"]=f"{round(value, 2)}\N{DEGREE CELSIUS}"
    
window=tk.Tk()
window.title("Temperature Converter")
window.resizable(False, False)  

window.rowconfigure(0, minsize=50)
window.columnconfigure([0,2], minsize=50)

entry=tk.Entry(master=window, width=10)
entry.grid(row=0, column=0, padx=10)

label_f=tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")
label_f.grid(row=0, column=1)

btn=tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert_c)
btn.grid(row=0, column=2)

label_c=tk.Label(master=window, text="\N{DEGREE CELSIUS}")
label_c.grid(row=0, column=3, padx=10)

window.mainloop()


