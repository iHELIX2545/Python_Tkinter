import tkinter as tk

window = tk.Tk() # to create structure/window

label1=tk.Label(text="Hello World", fg="red", bg="yellow", width=10, height=3) # to create a widget (+ attributes of the widget)
label1.pack() # to add the widget, to the window

button1=tk.Button(text="Click Me", fg="yellow", bg="red", height=3, width=10, borderwidth=0) # to create clickable widget
button1.pack()

# entry1=tk.Entry(fg="yellow", bg="blue", width=50) # to get a little bit of text from a user
# entry1.pack()
# entry1.get()
# entry1.delete(0,tk.END)

text_box = tk.Text(width=35, height=5, bg="grey")
text_box.pack()
# text_box.get("1.0", tk.END)       #to take input
text_box.insert("1.0", "HELLO")
text_box.insert(tk.END, "\nWorld")
text_box.delete("1.0")

frame_a=tk.Frame()  # frame == empty containers. An empty Frame widget is practically invisible.
label_a=tk.Label(master=frame_a, text="I'm in frame A", bg="green", height=5) # assign a widget to a frame by setting the widget’s master attribute
label_a.pack()
frame_a.pack()



window.mainloop()  # to run the event loop
































""" 
Widget Class	Description
------------    ------------
Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Frame	        A rectangular region used to group related widgets or provide padding between widgets
Text	        A text entry widget that allows multiline text entry
Entry	        A text entry widget that allows only a single line of text
 """