import tkinter as tk

window=tk.Tk()
window.title("Address Entry Form")

frame1=tk.Frame(master=window, relief="sunken", borderwidth=3)
frame1.pack()

label1=tk.Label(master=frame1, text="First Name : ")
label1.grid(row=0, column=0, sticky="e")
text_box1=tk.Text(master=frame1, height=1, width=50)
text_box1.grid(row=0, column=1)

label2=tk.Label(master=frame1, text="Last Name : ")
label2.grid(row=1, column=0, sticky="e")
text_box2=tk.Text(master=frame1, height=1, width=50)
text_box2.grid(row=1, column=1)

label3=tk.Label(master=frame1, text="Address 1 : ")
label3.grid(row=2, column=0, sticky="e")
text_box3=tk.Text(master=frame1, height=1, width=50)
text_box3.grid(row=2, column=1)

label4=tk.Label(master=frame1, text="Adrees 2 : ")
label4.grid(row=3, column=0, sticky="e")
text_box4=tk.Text(master=frame1, height=1,width=50)
text_box4.grid(row=3, column=1)

label5=tk.Label(master=frame1, text="City : ")
label5.grid(row=4, column=0, sticky="e")
text_box5=tk.Text(master=frame1, height=1,width=50)
text_box5.grid(row=4, column=1)

label6=tk.Label(master=frame1, text="Country : ")
label6.grid(row=5, column=0, sticky="e")
text_box6=tk.Text(master=frame1, height=1,width=50)
text_box6.grid(row=5, column=1)

frame2=tk.Frame()
frame2.pack(fill=tk.X, ipadx=5, ipady=5)

button2=tk.Button(master=frame2, text="Submit")
button2.pack(side=tk.RIGHT, padx=5, ipadx=10)

button1=tk.Button(master=frame2, text="Clear")
button1.pack(side=tk.RIGHT, padx=5, ipadx=10)

window.mainloop()