import tkinter as tk
from tkinter import ttk

CONVERSION_FACTORS = {
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Foot": 3.28084,
}

window = tk.Tk()
window.title("Length Converter")


# length conversion
def convert_length():
    value = float(entry_value.get())
    from_unit = cmb_from_unit.get()
    to_unit = cmb_to_unit.get()

    result = value * CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]
    label_result["text"] = "Converted Value: "+ str(round(result, 4))


label_value = ttk.Label(window, text="Value:")
label_value.grid(row=0,column=0, padx=5, pady=5)

entry_value = ttk.Entry(window)
entry_value.grid(row=0,column=1, padx=5, pady=5)

label_from_unit = ttk.Label(window, text="From Unit:")
label_from_unit.grid(row=1,column=0, padx=5, pady=5)

cmb_from_unit = ttk.Combobox(window, values=list(CONVERSION_FACTORS.keys()))
cmb_from_unit.grid(row=1,column=1, padx=5, pady=5)

label_to_unit = ttk.Label(window, text="To Unit:")
label_to_unit.grid(row=2,column=0, padx=5, pady=5)

cmb_to_unit = ttk.Combobox(window, values=list(CONVERSION_FACTORS.keys()))
cmb_to_unit.grid(row=2,column=1, padx=5, pady=5)

button_covert = ttk.Button(window, text="Convert", command=convert_length)
button_covert.grid(row=3,column=0, padx=5, pady=5)

label_result = ttk.Label(window, text="")
label_result.grid(row=3,column=1, padx=5, pady=5)

window.mainloop()
