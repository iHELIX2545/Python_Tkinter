import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    try:
        password_length=int(entry_length.get())
    except ValueError:
        lbl_result.config(text="Please enter a valid number") # use config to show the result in the app
        return
    
    char_sets=[]  # all checkbox selected options will create a character set(list) which will be used to generate random characters
    if upper_var.get():
        char_sets.append(string.ascii_uppercase)  # if checkbox value is 1, insert the uppercase letter type to the set
    if lower_var.get():
        char_sets.append(string.ascii_lowercase)
    if digits_var.get():
        char_sets.append(string.digits)
    if special_var.get():
        char_sets.append(string.punctuation)

    if not char_sets:
        lbl_result.config(text="Please select at least 1 option")
        return

    # implementation
    selected_types="".join(char_sets)  # selected_types -> creating a  string of selected options from the char_set list
    password="".join(random.choice(selected_types) for i in range(password_length))  
    """ here,
        randomly generating characters from the selected types using random() function and for loop,
        then concateting  it to a string using join() function """

    #show result
    lbl_result.config(text="Generated Password: "+ password)



window=tk.Tk()
window.title("Password generator")
window.resizable(False, False)

pad={"padx": 25, "pady":15}

lbl_top=ttk.Label(window, text="Password Generator", font=("Tw Cen MT", 15, "bold"))
lbl_top.pack(**pad)

lbl_length = ttk.Label(window, text="Password Length:")
lbl_length.pack(padx=25)
entry_length=ttk.Entry(window)
entry_length.pack(padx=25)

frame2=tk.Frame(window)
frame2.pack(**pad)
lbl_checkbox = ttk.Label(frame2, text="Include options: ")
lbl_checkbox.pack(padx=25)

upper_var=tk.IntVar()
upper_chk_btn=ttk.Checkbutton(frame2, text="Upper case letters", variable=upper_var)
upper_chk_btn.pack(padx=25)

lower_var=tk.IntVar()
lower_chk_btn=ttk.Checkbutton(frame2, text="Lower case letters", variable=lower_var)
lower_chk_btn.pack(padx=25)

digits_var=tk.IntVar()
digits_chk_btn=ttk.Checkbutton(frame2, text="Digits", variable=digits_var)
digits_chk_btn.pack(padx=25, anchor=tk.W)

special_var=tk.IntVar()
special_chk_btn=ttk.Checkbutton(frame2, text="Special characters", variable=special_var)
special_chk_btn.pack(padx=25)

frame_3=tk.Frame(window)
frame_3.pack(**pad)

btn_generate = ttk.Button(frame_3, text="Generate Password", command=generate_password)
btn_generate.pack(padx=25)

lbl_result = ttk.Label(frame_3, text="", font=("Tw Cen MT", 12, "bold"))
lbl_result.pack(padx=25)

window.mainloop()

""" 
 --> characters="".join(character_sets)  <--
The character_sets list is joined using the join method to create a single string called all_characters.
This string will contain all the characters that were selected for generating the password.

 --> generated_password = ''.join(random.choice(selected_types) for _ in range(password_length)) <--
The random.choice function is used to randomly select a single character from the all_characters string
then the loop repeats password_length times to randomly generate characters for the password
 """