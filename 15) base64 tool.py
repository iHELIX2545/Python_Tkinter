import tkinter as tk 
from tkinter import ttk 
import base64

def encode_text():
    # get text -> encode(ascii) -> base64 encode -> insert
    input_text = text_input.get("1.0", "end") # "1.0", "end" --> to take all characters from the text field
    text_byte=input_text.encode("ascii")    # converting to ascii form
    base64_byte = base64.b64encode(text_byte)   # converting to base64 (byte form)
    
    text_output.delete("1.0", "end")    # clearing the output text field
    text_output.insert("1.0", base64_byte.decode())     # decode the base64_byte and showing in output field 

def decode_text():
    # get text -> encode(ascii) -> base64 decode -> insert
    input_text = text_input.get("1.0", "end")
    try:
        text_byte=input_text.encode("ascii")
        base64_byte = base64.b64decode(text_byte) 

        text_output.delete("1.0", "end")
        text_output.insert("1.0", base64_byte.decode())

    # if > base64.binascii.Error < this error shows, throw "Invalid Base64 input!"
    except base64.binascii.Error:   # if 
        text_output.delete("1.0", "end")
        text_output.insert("1.0", "Invalid Base64 input!")

# Create the main window
window = tk.Tk()
window.title("Base64 Tool")

frame1=ttk.Frame(window)
frame1.pack(pady=2)
lbl_input = ttk.Label(frame1, text="Input:")
lbl_input.pack()
text_input = tk.Text(frame1, height=10, width=50, relief="flat")
text_input.pack(pady=5)

btn_encode = ttk.Button(frame1, text="Encode", command=encode_text)
btn_encode.pack()
btn_decode = ttk.Button(frame1, text="Decode", command=decode_text)
btn_decode.pack()

frame2=ttk.Frame(window)
frame2.pack()
lbl_output = tk.Label(frame2, text="Output:")
lbl_output.pack(pady=2)
text_output = tk.Text(frame2, height=10, width=50, relief="flat")
text_output.pack()

window.mainloop()
