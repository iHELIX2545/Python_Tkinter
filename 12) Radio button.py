import tkinter as tk


def selected_option():
    temp=entry.get()     # retrieves the entry value (which is a string)
    selected=var.get()    # retrieves the selected option value from var
    if selected==1:
        temp=(float(temp) * 9/5) + 32
        label_result["text"]="Result: "+ str(temp)+" \N{DEGREE FAHRENHEIT}"

    if selected==2:
        temp=(float(temp) - 32) * 5/9
        label_result["text"]="Result: " + str(temp) + " \N{DEGREE CELSIUS}"


window = tk.Tk()

var=tk.IntVar()  # IntVar() to hold the selected option value
var.set(1) # Default to Celsius to Fahrenheit

option1=tk.Radiobutton(master=window, variable=var, text="Celsius to Fahrenheit", value=1)
option1.grid(row=0, column=0)

option2=tk.Radiobutton(master=window, variable=var, text="Fahrenheit to Celsius", value=2)
option2.grid(row=1, column=0)

entry=tk.Entry(master=window, width=20, relief="sunken")
entry.grid(row=2, column=0,padx=20, pady=10)

btn_submit=tk.Button(master=window, text="Submit", command=selected_option)
btn_submit.grid(row=3, column=0,padx=20, pady=10)

label_result=tk.Label(master=window, font=("Arial", 12, "bold"))
label_result.grid(row=4,column=0,padx=20, pady=10)

window.mainloop()


""" 
* Use ttk.Radiobutton(text, variable) to create a radio button; 
* the variable should be a tk.IntVar() or tk.StringVar()
* A set of radio buttons share the same variable.
* the radio buttons must have value to operate properly
 """


""" 
Each radio button has a different value. However, radio buttons in the same group share the same variable.

master -> is the parent widget which you place the radio buttons on.
text -> argument specifies the text that appears on the radio button.
** value -> argument specifies the value that the radio button will hold. 
** variable -> must be a tk.IntVar() or tk.StringVar()
 """
