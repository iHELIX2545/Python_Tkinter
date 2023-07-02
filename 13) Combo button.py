from tkinter import *
from tkinter import ttk

def menu_select():
    label_result["text"]=str(cmb_menu.get())

window = Tk()
window.title('Combobox')

menu = ["Pizza", "Burger", "Noodles"]

label1 = Label(window, text="Choose Your Favorite Food")
label1.grid(column=0, row=0)

cmb_menu = ttk.Combobox(window, values=menu, width=30)
cmb_menu.grid(column=0, row=1)
# cmb_menu.current(0)

btn_enter = Button(window, text="Enter", command=menu_select)
btn_enter.grid(column=0, row=2)

label_result = Label(window, text="")
label_result.grid(column=0, row=3)



window.mainloop()


""" 
Options     	Descriptions
-------         ------------
justify	        The alignment of text within the widget.
height	        The height of the pop-down listbox.
postcommand	    It is called immediately before displaying the values.
textvariable	It specifies a name whose value is linked to the widget value.
values	        It specifies the list of values to display in the drop-down listbox.
width	        It specifies the width of the entry window.

 """
