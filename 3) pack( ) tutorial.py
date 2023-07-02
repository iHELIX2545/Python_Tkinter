import tkinter as tk

window = tk.Tk()

frame1=tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, expand=True)


frame2=tk.Frame(master=window, width=50, height=50, bg="blue")
frame2.pack(fill=tk.BOTH,  expand=True)

frame3=tk.Frame(master=window, width=25, height=25, bg="green")
frame3.pack(fill=tk.BOTH, expand=True)


frame4=tk.Frame(master=window, width=150, height=150, bg="blue")
frame4.pack()

label1= tk.Label(master=frame4, text="I'm at(0,0)", bg="yellow")
label1.place(x=0, y=0)

label2= tk.Label(master=frame4, text="I'm at(75,75)", bg="green")
label2.place(x=75, y=75)




window.mainloop()


""" 
=> geometry managers:
1) .place()
2) .grid()

--> .pack() is an example of a geometry manager
--> each Frame is centered in the window unless we use anchor attribute
--> fill keyword argument to specify in which direction the frames should fill """


""" 
=> .pack(fill= ____ )
We can set the fill keyword argument to specify in which direction the frames should fill. 
The options are:
    --> tk.X to fill in the horizontal direction
    --> tk.Y to fill vertically, and 
    --> tk.BOTH to fill in both directions.
pros: filling the window with .pack() is that it's responsive to window resizing."""


""" 
To make the layout truly responsive and resizable:
--> set an initial size for your frames using the width and height attributes. 
--> Then, set fill = tk.BOTH and
--> set expand = True  """


""" 
=> .pack(side= ____ )
The side keyword argument of .pack() specifies on which side of the window the widget should be placed. 
These are the available options:
    -> tk.TOP
    -> tk.BOTTOM
    -> tk.LEFT
    -> tk.RIGHT """


""" 
=> .place() to control the precise location that a widget should occupy in a window or Frame

We must provide two keyword arguments. x and y, which specify:
    --> the x- and y-coordinates for the top-left corner of the widget.
    --> Both x and y are measured in pixels
    --> .place(x=0, y=0) is the top left corner of the frame/window

.place() has many drawbacks, so used only occasionally """