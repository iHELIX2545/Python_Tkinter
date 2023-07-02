import tkinter as tk

# for command method, we must define the function before creating the button
def btn2_click():
    print("Button-2  was clicked")

window = tk.Tk()

# button - 1 used for .bind method
button_1 = tk.Button(master=window, text="Button 1")
button_1.pack()

# button - 2 used with command method
button_2 = tk.Button(master=window, text="Button 2", command=btn2_click)
button_2.pack()


# btn1_click function & what it does afterward
def btn1_click(event):
    print("Button-1  was clicked")

# binding the button1 with the event
button_1.bind("<Button-1>", btn1_click)

window.mainloop()










# command method is easier and easy to understand.

""" 
    "<Button-1>" => event
    btn_click() => event handler
    * To bind an event handler to any button => button.bind("<__>", func_name) """

""" 
.bind() takes at least two arguments:
    -> "<event_name>" : An event, where event_name can be any of Tkinter's events
    -> function name : An event handler that's the name of the function to be called whenever the event occurs """