import tkinter as tk

window=tk.Tk()

frame1=tk.Frame(master=window, bg="yellow")
frame1.pack()

for r in range(3):
    window.columnconfigure(r, weight=1, minsize=75)
    window.rowconfigure(r, weight=1, minsize=50)

    for c in range(3):
        frame=tk.Frame(master=frame1, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=r, column=c, padx=5, pady=10)
        label=tk.Label(master=frame, text=f"Row {r}\nColumn {c}")
        label.pack(padx=50, pady=10)


window.mainloop()


# import tkinter as tk
# window = tk.Tk()

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)

# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")

# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")

# window.mainloop()




""" 
=> best geometry manager: .grid()
The important thing to realize here is that 
    even though .grid() is called on each Frame object, the geometry manager applies to the window object. 
    Similarly, the layout of each frame is controlled with the .pack() geometry manager.

--> padx adds padding in the horizontal direction.
--> pady adds padding in the vertical direction.

 """